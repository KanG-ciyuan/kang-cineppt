<div align="center">

![Kang CinePPT](docs/assets/cover.png)

# kang-cineppt

**Cinematic motion slides. Editable type. Deliberate timing.**<br>
An Agent Skill for AI-assisted motion PPTs and optional promotional films.

![Version](https://img.shields.io/badge/version-v0.1.0-1a455d?style=flat-square)
[![Code MIT](https://img.shields.io/badge/code-MIT-d5b37a?style=flat-square)](LICENSE)
[![Case Keynote](https://img.shields.io/badge/case-Keynote%20checked-277c86?style=flat-square)](docs/VALIDATION.md)

[中文](README.md) · [English](README.en.md)

</div>

Combine full-frame moving backgrounds with native editable typography and restrained entrance animations. Deliver an editable PPTX master and, when requested, an MP4 for promotion.

## The actual case

[![Toward the Open Sea — actual film preview](docs/assets/demo.gif)](docs/assets/xiang-hai-er-xing.mp4)

Click for the complete MP4 preview. Ocean footage is AI-generated; the GIF and smaller MP4 are display derivatives of the existing finished film, not new test works.

| Cargo ship | Giant wave and sailboat |
|---|---|
| ![Cargo ship slide](docs/assets/slide-1.jpg) | ![Wave slide](docs/assets/slide-2.jpg) |

**Evidence:** “Toward the Open Sea” was produced, opened, played, and exported in Keynote before this Skill was packaged. The owner watched and approved the result. This Skill package has received static review only. It has not been installed, reproduced in another Agent environment, or tested with a new end-to-end run. PowerPoint and WPS playback remain unverified. v0.1.0 is an early, case-derived method package; installation and cross-environment operation are not verified.

## Example requests

- “Use this reference to make two cinematic motion slides, with editable titles and rules.”
- “Keep the entire ocean moving. Start the ship scene first, then fade in all text.”
- “Do not restart the ship clip. Advance to the next scene before any loop reset.”
- “I need a promotional MP4 and an editable PPTX master. Confirm costs before paid generation.”

## Workflow and requirements

Reference analysis → scene plan → cost approval → generated or existing footage → local grading/interpolation → native editable slides → playback verification → optional movie export.

You need an Agent able to read Skill instructions and an authorized presentation-authoring tool. No Agent installation adapter is verified. Keynote has historical case evidence; other applications need their own playback checks. Use rights-cleared media and obtain approval for each paid generation scope. Optional helpers require Python 3.10+; local video processing also needs FFmpeg/FFprobe. No proprietary SDK, font, model, or application is bundled.

## Loading and helpers

Read [SKILL.md](SKILL.md) and load the directory using your Agent's documented mechanism. Download the source from [GitHub Releases](https://github.com/KanG-ciyuan/kang-cineppt/releases/tag/v0.1.0), or use your Agent’s documented loading mechanism. A common Agent Skills CLI form is shown below; **it was not executed or validated for this project**:

```bash
npx skills add KanG-ciyuan/kang-cineppt
```

No Skill installation, activation check, or Agent configuration change was performed for this release.

```bash
python3 scripts/inspect_pptx.py path/to/deck.pptx
python3 scripts/check_package.py
```

The first command inspects package structure only, without opening a presentation application. The second performs offline static checks and never runs creative helpers. The optional media recipe wrapper is statically reviewed but has no new runtime test evidence.

## Delivery and limits

Deliver the editable master, backgrounds, and requested film. Record structural evidence, actual playback application, movie properties, and human review separately. An XML timer is not proof of autoplay. Local 60fps interpolation is not native 60fps generation or 120fps footage.

Keep credentials in the host's secure configuration. Never automatically retry paid jobs, publish files, install tools, or change Agent configuration without authorization.

## Troubleshooting

| Symptom | Action |
|---|---|
| Ship jumps to its starting position | Disable discontinuous looping; play once and advance |
| Text finishes after the clip | Use one native group fade and complete it earlier |
| Text is visible in edit view | Test the full slideshow, not the video object alone |
| Motion still looks unnatural at 60fps | Inspect wave edges, wake and hull interpolation artifacts |
| Layout changes on another device | Resolve font substitution and verify in the target app |

## License and publication

Authored code and documentation use the [MIT License](LICENSE). Demonstration media are excluded; no blanket asset redistribution or commercial-use license is granted. Proprietary tools, system fonts, account data and the third-party reference video are not included.

See [third-party notices](THIRD_PARTY_NOTICES.md) for the media-rights and provider-disclosure boundaries. The owner confirmed the reviewed publication and case-display scope; no blanket media reuse or provider endorsement is claimed. Detailed workflow documents are currently Chinese-first.

[Case study](docs/CASE-STUDY.md) · [Validation](docs/VALIDATION.md) · [Release notes](docs/RELEASE-NOTES.md)
