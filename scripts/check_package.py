#!/usr/bin/env python3
"""Offline static lint. Does not run helpers, install, generate, contact APIs or play PPTs."""
# Copyright (c) 2026 Kang. MIT License; see ../LICENSE.
import argparse
import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote


def check(root):
    findings = []
    files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
    required = ['SKILL.md', 'README.md', 'README.en.md', 'LICENSE', 'manifest.json',
                'agents/interface.yaml', 'THIRD_PARTY_NOTICES.md', 'docs/VALIDATION.md',
                'references/workflow.md', 'references/visual-standard.md', 'references/acceptance.md']
    for name in required:
        if not (root/name).is_file():
            findings.append({'file': name, 'kind': 'missing_required'})
    entries = [p.relative_to(root).as_posix() for p in files if p.name == 'SKILL.md']
    if entries != ['SKILL.md']:
        findings.append({'kind': 'skill_entrypoint_count', 'count': len(entries)})
    manifest = json.loads((root/'manifest.json').read_text())
    skill = (root/'SKILL.md').read_text()
    if not skill.startswith('---\n') or 'name: kang-cineppt\n' not in skill:
        findings.append({'file': 'SKILL.md', 'kind': 'frontmatter'})
    if manifest['name'] != 'kang-cineppt' or manifest['version'] != '0.1.0':
        findings.append({'file': 'manifest.json', 'kind': 'identity_version'})
    if len(skill.encode()) > 14000:
        findings.append({'file': 'SKILL.md', 'kind': 'oversized_entrypoint'})
    text_suffixes = {'.md', '.py', '.json', '.yaml', '.yml', '.svg', '.txt'}
    patterns = {
        'private_absolute_path': r'/(?:Users|home)/[A-Za-z0-9_.-]+/',
        'windows_private_path': r'[A-Z]:\\(?:Users|Documents)\\',
        'credential_token': r'\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,})',
        'private_key': r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----',
        'signed_media_url': r'https?://[^\s<>]+[?&](?:token|signature|credential|X-Amz-Signature)=',
    }
    for p in files:
        relative = p.relative_to(root).as_posix()
        if p.is_symlink():
            findings.append({'file': relative, 'kind': 'symlink'})
        if p.name in {'.env', 'auth.json', 'credentials.json', '.DS_Store'} or p.suffix in {'.pem', '.key', '.pyc'}:
            findings.append({'file': relative, 'kind': 'forbidden_file'})
        if p.stat().st_size >= 100 * 1024 * 1024:
            findings.append({'file': relative, 'kind': 'github_file_size'})
        if p.suffix not in text_suffixes and p.name not in {'LICENSE', '.gitignore', '.gitattributes'}:
            continue
        content = p.read_text()
        for kind, pattern in patterns.items():
            if re.search(pattern, content):
                findings.append({'file': relative, 'kind': kind})
        if p.suffix == '.json':
            json.loads(content)
        if p.suffix == '.py':
            ast.parse(content, filename=relative)
        if p.suffix == '.md':
            for destination in re.findall(r'\]\(([^)]+)\)', content):
                if destination.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                target = (p.parent/unquote(destination.split('#')[0])).resolve()
                if not target.exists() or not target.is_relative_to(root.resolve()):
                    findings.append({'file': relative, 'kind': 'broken_local_link', 'target': destination})
    return {
        'kind': 'static_review_only', 'ok': not findings,
        'files_checked': len(files), 'python_syntax_checked': sum(p.suffix == '.py' for p in files),
        'findings': findings,
        'not_run': ['installation', 'agent_activation', 'new_provider_calls',
                    'new_test_works', 'helper_runtime_validation', 'new_end_to_end_tests'],
        'publication': 'requires_owner_approval_and_media_rights_confirmation',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = check(args.root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['ok'] else 1)


if __name__ == '__main__':
    main()
