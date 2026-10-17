#!/usr/bin/env python3
"""Read-only PPTX structure summary; never proves application playback."""
# Copyright (c) 2026 Kang. MIT License; see ../LICENSE.
import argparse
import hashlib
import json
import posixpath
from pathlib import Path
from zipfile import ZipFile, BadZipFile
import xml.etree.ElementTree as ET

NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}
XML_LIMIT = 10 * 1024 * 1024


def read_xml(z, name):
    if z.getinfo(name).file_size > XML_LIMIT:
        raise ValueError('XML part exceeds the inspection limit.')
    raw = z.read(name)
    if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:
        raise ValueError('DTD/entity declarations are not accepted.')
    return ET.fromstring(raw)


def inspect(path):
    report = {'structural_only': True, 'application_playback_verified': False,
              'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'slides': []}
    with ZipFile(path) as z:
        names = set(z.namelist())
        if len(names) > 5000:
            raise ValueError('Too many ZIP members for this lightweight inspector.')
        presentation = read_xml(z, 'ppt/presentation.xml')
        size = presentation.find('p:sldSz', NS)
        report['slide_size_emu'] = dict(size.attrib) if size is not None else None
        rels = read_xml(z, 'ppt/_rels/presentation.xml.rels')
        rel_by_id = {e.get('Id'): e for e in rels}
        ids = presentation.find('p:sldIdLst', NS)
        if ids is None:
            raise ValueError('No slide list found.')
        for number, item in enumerate(ids, 1):
            rid = item.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            relation = rel_by_id[rid]
            if relation.get('TargetMode') == 'External':
                raise ValueError('External slide relation is unsupported.')
            target = relation.get('Target', '')
            part = (target.lstrip('/') if target.startswith('/') else
                    posixpath.normpath(posixpath.join('ppt', target)))
            slide = read_xml(z, part)
            relpart = posixpath.join(posixpath.dirname(part), '_rels', posixpath.basename(part)+'.rels')
            videos = []
            if relpart in names:
                for rel in read_xml(z, relpart):
                    if not rel.get('Type', '').endswith(('/video', '/media')):
                        continue
                    media = rel.get('Target', '')
                    external = rel.get('TargetMode') == 'External'
                    resolved = (media.lstrip('/') if media.startswith('/') else
                                posixpath.normpath(posixpath.join(posixpath.dirname(part), media)))
                    videos.append({'external': external,
                                   'embedded_member_exists': not external and resolved in names})
            anim = slide.findall('.//p:animEffect', NS)
            transition = slide.find('p:transition', NS)
            report['slides'].append({
                'number': number,
                'native_text_runs': len(slide.findall('.//a:t', NS)),
                'native_groups': len(slide.findall('.//p:grpSp', NS)),
                'media_relationships': videos,
                'fade_effects': sum('fade' in e.get('filter', '').lower() for e in anim),
                'repeat_counts': [e.get('repeatCount') for e in slide.findall('.//p:cTn', NS)
                                  if e.get('repeatCount') is not None],
                'transition_attributes': dict(transition.attrib) if transition is not None else {},
            })
        report['slide_count'] = len(report['slides'])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pptx', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.pptx), ensure_ascii=False, indent=2))
    except (OSError, KeyError, ValueError, BadZipFile, ET.ParseError) as error:
        # Do not dump document text, absolute paths, external URLs or credentials.
        parser.exit(2, 'PPTX structure inspection failed ('+type(error).__name__+').\n')


if __name__ == '__main__':
    main()
