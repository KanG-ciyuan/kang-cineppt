#!/usr/bin/env python3
"""Optional local recipe wrapper; no provider API. Runtime portability unverified."""
# Copyright (c) 2026 Kang. MIT License; see ../LICENSE.
import argparse
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--look', choices=['preserve', 'ship-bright'], default='preserve')
    args = parser.parse_args()
    source, target = args.input.resolve(), args.output.resolve()
    if not source.is_file():
        parser.error('Input video does not exist.')
    if source == target or target.exists():
        parser.error('Use a new output path; originals are never overwritten.')
    if target.suffix.lower() != '.mp4':
        parser.error('Output must use the .mp4 extension.')
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg:
        parser.error('FFmpeg must already be installed and authorized.')
    filters = []
    if args.look == 'ship-bright':
        filters.extend([
            'eq=brightness=0.025:contrast=1.03:gamma=1.25:saturation=1.16',
            'colorbalance=bs=0.04:bm=0.055:rs=-0.01:rm=-0.01',
        ])
    filters.append('minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir')
    target.parent.mkdir(parents=True, exist_ok=True)
    # This background-only recipe deliberately drops audio. Do not use for a mixed film.
    subprocess.run([
        ffmpeg, '-n', '-hide_banner', '-loglevel', 'error', '-i', str(source),
        '-vf', ','.join(filters), '-c:v', 'libx264', '-preset', 'medium',
        '-crf', '18', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', str(target),
    ], check=True)
    print('Created a local interpolated background. Inspect motion artifacts before use.')


if __name__ == '__main__':
    main()
