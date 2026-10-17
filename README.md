<div align="center">

![Kang CinePPT 电影感动态PPT](docs/assets/cover.png)

# kang-cineppt

**让海浪铺满画面，让文字按节奏出现。**<br>
AI电影感动态PPT制作技能 · 可编辑母版 + 宣传成片

![Version](https://img.shields.io/badge/version-v0.1.0-1a455d?style=flat-square)
[![Code MIT](https://img.shields.io/badge/code-MIT-d5b37a?style=flat-square)](LICENSE)
[![Case Keynote](https://img.shields.io/badge/case-Keynote%20checked-277c86?style=flat-square)](docs/VALIDATION.md)

[中文](README.md) · [English](README.en.md) · [制作流程](references/workflow.md) · [验证边界](docs/VALIDATION.md)

</div>

把AI或已有的视频背景、可编辑中文排版、克制的原生淡入和真实放映节奏组合起来。交付PPTX母版，也可导出用于宣传的MP4。

## 先看实际成片

[![向海而行实际成片的动态预览](docs/assets/demo.gif)](docs/assets/xiang-hai-er-xing.mp4)

**点击预览查看完整MP4。** 动态预览来自已完成的《向海而行》，背景为AI生成，GIF仅是低帧率展示副本。[案例与制作记录](docs/CASE-STUDY.md)

| 向海而行 | 共赴远方 |
|---|---|
| ![货轮PPT效果](docs/assets/slide-1.jpg) | ![巨浪帆船PPT效果](docs/assets/slide-2.jpg) |
| 视频先开始，全部文字统一淡入 | 巨浪与帆船建立尺度反差，字幕及早完成 |

**证据范围：** 原案例已完成制作、Keynote放映与导出，作者观看认可。v0.1 Skill包仅完成静态审查；未安装、未在其他Agent复现、未生成新测试作品，也未运行新的端到端测试。v0.1.0是基于实际案例整理的早期方法包，安装与跨环境能力不作已验证声明。

## 你可以直接这样说

- “参考这个视频，先做两页电影感动态PPT，标题和线条都能编辑。”
- “整页都是流动海面，船先入场，再让所有文字淡入。”
- “货轮不要循环回到起点，播放结束直接切到下一页。”
- “最后我要发宣传视频，同时保留PPTX母版；付费生成前先确认预算。”

## 它负责什么

参考分析 → 动态素材计划 → 费用确认 → 背景生成或复用 → 本地调色补帧 → 原生PPT排版和动画 → 目标软件实播 → 可选MP4导出。

它提供制作判断和编排方法。实际画面生成、母版构建和影片导出由宿主已合法提供的工具完成；不附模型、演示软件、专有SDK或自动上传服务。

## 前置条件

- [ ] 一个能够读取Skill指令并操作文件/演示软件的Agent；本包尚未验证任何Agent安装适配。
- [ ] 已授权的演示工具或原生软件。Keynote仅有案例级验证，PowerPoint/WPS需自行实播。
- [ ] 具有使用与展示权的背景素材。新AI视频生成需要自己的服务账户、实际费用确认和明确授权。
- [ ] 可选Python 3.10+：`python3 --version`；辅助脚本只用标准库。
- [ ] 可选FFmpeg/FFprobe：`ffmpeg -version`、`ffprobe -version`，用于本地修整与媒体检查。

字体可替换为目标机器合法可用的字体，替换后核对版式。本包不要求安装私有`@oai/artifact-tool`。

## 获取与使用

阅读根目录[SKILL.md](SKILL.md)，由你使用的Agent按其官方方式载入。把完整目录保持在一起，以便读取`references/`。

公开仓库：[KanG-ciyuan/kang-cineppt](https://github.com/KanG-ciyuan/kang-cineppt)。可下载[Release源码包](https://github.com/KanG-ciyuan/kang-cineppt/releases/tag/v0.1.0)。

常用Agent Skills CLI写法如下，**本项目未执行该安装命令，也未验证安装与激活**：

```bash
npx skills add KanG-ciyuan/kang-cineppt
```

请按你的Agent官方机制选择是否安装。本次发布没有安装Skill或修改作者的Agent配置。

## 辅助脚本

```bash
# 只读检查现有PPTX结构，不启动放映
python3 scripts/inspect_pptx.py path/to/deck.pptx

# 本仓库的离线静态检查，不运行创作脚本
python3 scripts/check_package.py
```

可选转码配方见[媒体处理](references/media-recipes.md)。本次没有运行新素材转码来验证该辅助脚本。旧案例中依赖专有SDK与样本XML的构建包装未随包分发，详见[原生制作方法](references/native-authoring.md)。

## 交付与验收

交付可编辑PPTX、背景素材和用户要求的MP4。验收分别记录包结构、目标软件实际放映、成片参数与观看结果；不能只靠“文件生成成功”。[完整验收标准](references/acceptance.md)

密钥只由宿主安全配置提供，不写入提示词示例、代码或报告。不自动重试付费调用，不默认上传、发布、安装或改Agent配置。

## Troubleshooting

| 现象 | 原因与处理 |
|---|---|
| 货轮回到起点 | 素材首尾不连续；关闭循环，单次播放后切页 |
| 字幕出不完背景先停 | 对象延迟累加；短片用一组一次淡入，提前出字并实播 |
| 编辑态文字全在 视频单独播放没有淡入 | 编辑态及媒体预览不代表整页时序；从页首完整放映 |
| 60fps仍不自然 | 插值不能修复所有运动问题；观察浪边和船体，不只看帧率 |
| 换机器排版变化 | 字体替换或跨软件时序差异；换合法字体并重新放映 |

## 许可证与发布状态

作者代码与文档：[MIT](LICENSE)。演示媒体与字体等外部权利独立处理，**不随MIT授予素材复用权**。原始第三方参考视频、账户信息、私有工具代码和系统字体均已排除。

[第三方及素材授权核对](THIRD_PARTY_NOTICES.md)列明供应商输出权利与公开展示/服务商披露条款的待确认事项。作者已确认本次公开清单及案例展示范围。媒体不附普遍复用许可，也不声称取得供应商官方背书；第三方再使用应自行核对相关权利与条款。

[v0.1.0发布说明](docs/RELEASE-NOTES.md) · [公开范围与确认记录](docs/PUBLICATION-REVIEW.md)
