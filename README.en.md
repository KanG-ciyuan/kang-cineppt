<div align="center">

![Kang CinePPT](docs/assets/cover.png)

# kang-cineppt

**Cinematic motion slides for real presentation endings.**<br>
Full-frame footage · Editable typography · Native fades · Optional MP4

![Version](https://img.shields.io/badge/version-v0.2.0-1a455d?style=flat-square)
[![Code MIT](https://img.shields.io/badge/code-MIT-d5b37a?style=flat-square)](LICENSE)
[![Case Keynote](https://img.shields.io/badge/cases-Keynote%20checked-277c86?style=flat-square)](docs/VALIDATION.md)

[中文](README.md) · [English](README.en.md) · [Case library](docs/CASE-LIBRARY.md)

</div>

An Agent Skill for combining moving backgrounds, native editable Chinese typography and restrained fades. Deliver an editable PPTX and an optional promotional MP4. Work from existing footage, free licensed live-action clips, or explicitly approved paid generation.

## Watch the new cases

| Riding the Momentum | Homeland in Mind |
|---|---|
| [![Ocean case excerpt](docs/assets/chengshi-er-shang/demo.gif)](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/chengshi-er-shang-18s-1080p.mp4) | [![Flag and Great Wall case excerpt](docs/assets/shanhe-zaixin/demo.gif)](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/shanhe-zaixin-18s-1080p.mp4) |
| Giant waves, a small surfer, and quiet ocean space for a team presentation ending. | A waving Chinese flag followed by the Great Wall, composed for a solemn presentation ending. |
| [Full film, 18s](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/chengshi-er-shang-18s-1080p.mp4) · [Editable PPTX](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/chengshi-er-shang-18s.pptx) | [Full film, 18s](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/shanhe-zaixin-18s-1080p.mp4) · [Editable PPTX](https://github.com/KanG-ciyuan/kang-cineppt/releases/download/v0.2.0/shanhe-zaixin-18s.pptx) |

GIFs are low-frame-rate excerpts of actual finished films. The full 1080p/30fps videos use actual Keynote exports followed by trimming and licensed music synchronization. Both new showcase cases use free licensed real footage, with no paid video-generation call. [Sources and licenses](docs/MEDIA-SOURCES.md)

### Original case: Toward the Open Sea

[![Original ocean case](docs/assets/demo.gif)](docs/assets/xiang-hai-er-xing.mp4)

AI-generated ocean backgrounds with editable native type. [Original case study](docs/CASE-STUDY.md)

[Between Heaven and Earth](docs/cases/tiandi-zhijian.md) is retained as an exploration, including the feedback that its first scene lacked impact. Its promotional film was composed separately with FFmpeg; it is not a native PPT movie export.

**Evidence boundary:** The works have their own case-specific Keynote records. This Skill release has static checks only. It has not been installed, activated or reproduced in another Agent environment, and no new end-to-end test was run for publication. Microsoft PowerPoint and WPS playback remain unverified. [Validation](docs/VALIDATION.md)

## Example requests

- “Find two free licensed live-action clips. Let me approve the motion and color before making two editable closing slides.”
- “Keep the whole ocean moving and use scale contrast. Fade in all native text early.”
- “Create a solemn patriotic presentation ending using a flag and the Great Wall.”
- “I need an MP4 and an editable PPTX. Confirm the cost before paid generation.”

## Loading and prerequisites

Read [SKILL.md](SKILL.md) and load the complete directory through your Agent's documented mechanism. [Download v0.2.0](https://github.com/KanG-ciyuan/kang-cineppt/releases/tag/v0.2.0). A common CLI form is shown below; **installation and activation were not executed or validated for this project**:

```bash
npx skills add KanG-ciyuan/kang-cineppt
```

You need an Agent with file access and authorized native presentation-authoring tools. Keynote has case evidence only; other applications need their own playback checks. Optional helpers require Python 3.10+ and local video processing needs FFmpeg/FFprobe. No proprietary SDK, model, font or application is bundled. A private `@oai/artifact-tool` installation is not required by this package.

## Workflow

Define the presentation use → verify footage rights → preview motion and color → prepare backgrounds → author editable typography and embed video → test the actual slideshow → optionally export and inspect the film.

Prefer longer source footage before slowing a clip. Record source, processed and export frame rates separately. For multiple fades, convert the intended absolute timings into the application's relative delays. Check Keynote export waits and extra terminal frames in the actual output. [Workflow](references/workflow.md) · [Native authoring](references/native-authoring.md)

```bash
python3 scripts/inspect_pptx.py path/to/deck.pptx
python3 scripts/check_package.py
```

The first command inspects package structure without opening a slideshow. The second is offline static lint. Creative helpers remain statically reviewed only; case-specific production is not independent runtime proof for those helpers.

## Troubleshooting

| Symptom | Action |
|---|---|
| It feels like a landscape commercial | Establish the work-report purpose and closing copy first |
| Subject jumps to the starting position | Disable discontinuous looping and advance after one forward pass |
| Text completes after the clip ends | Reduce cumulative delays and reserve reading time |
| Text is visible in the editor | Test the full slideshow rather than the media object |
| Movie holds the last frame too long | Inspect added slide waits and terminal frames |
| Higher fps still feels unnatural | Inspect source motion and interpolation artifacts |
| Layout changes on another machine | Resolve fonts and verify in the target application |

## License

Authored code and documentation use [MIT](LICENSE). Demonstration footage, GIFs, screenshots and third-party media embedded in the downloadable PPTX files are **excluded from MIT**. Pexels footage and Mixkit music retain their own license conditions; the original AI case retains its separate rights notice. [Third-party notices](THIRD_PARTY_NOTICES.md)

No original reference footage, standalone source clips/music, system font files, secrets, private paths or proprietary runtime is included. A PPTX download is not a license to redistribute extracted stock media. No provider, creator or depicted subject endorsement is implied.

No Skill installation, new generation, test work, end-to-end creation test or Agent configuration change was performed for this update. [Release notes](docs/RELEASE-NOTES.md) · [Publication scope](docs/PUBLICATION-REVIEW.md)
