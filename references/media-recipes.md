# 本地媒体处理

以下配方来自既有案例，不会调用任何生成API。命令仅在用户授权创作或修整时运行；整理Skill和静态审查时不执行。始终输出新文件，不覆盖原片。

## 读取参数

```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames -show_entries format=duration -of json input.mp4
```

## 运动插值

`minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir`估计运动并补出中间帧，保持播放速度。其成本和浪花伪影需按素材判断；设置输出帧率本身不等于运动插值。

原货轮页使用`eq`与`colorbalance`提亮暗部。封装脚本提供`--look ship-bright`和`--look preserve`两种选择；固定数值是案例起点，不是自动调色算法。

```bash
python3 scripts/prepare_background.py --input input.mp4 --output background-60fps.mp4 --look preserve
```

此脚本为便于移植而从案例处理配方整理，**本次只做语法与安全静态检查，未运行新素材转码**。

## 原生影片重封装

```bash
ffmpeg -n -i keynote-export.m4v -map 0:v:0 -c:v copy -movflags +faststart film.mp4
```

这是本案例静音片的配方，`-map 0:v:0`不保留音频。需要配乐时显式选择音轨并重新验收音画；不要照搬后误删声音。

## 连续性辅助检查

```bash
ffmpeg -i film.mp4 -vf "freezedetect=n=-45dB:d=0.20,blackdetect=d=0.1:pix_th=0.1" -an -f null -
```

检测阈值属于技术证据，不能替代完整观看。对动态海面尤其需要同时看字幕完成、浪边变形、主体方向和切点。
