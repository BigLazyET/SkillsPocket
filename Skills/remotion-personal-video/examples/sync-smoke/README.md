# SyncSmoke 音画试片

这是 15 秒的可复跑测试工程。画面来自本地生成的模拟录屏，台词由 macOS 自带的 Tingting 合成。没有真实产品素材、外部媒体 URL 或社区 Skill 路径依赖。准备素材需要 macOS、Tingting、Python 3、FFmpeg 和 FFprobe，渲染需要 Node.js、npm 和 Remotion 支持的浏览器。

把这个目录复制到临时位置，再执行：

```bash
npm ci
python3 prepare.py
npm run studio
# 在另一个终端导出两个画幅
npm run render:wide
npm run render:tall
python3 verify.py
```

两份 MP4 都应为 30 fps、450 帧。首 2 秒是片头，字幕和旁白一起延后。模拟录屏跨过两段对白及中间的停顿。成片第 150 帧（5 秒）按钮变绿，同时响点击声。横版字幕两条，竖版把第二条拆成两条，仍对应同一台词段 U02。字幕超宽、超字数、帧区间无效或脱离台词段时，渲染会报错。`verify.py` 校验成片尺寸、帧数以及点击的画面和声音落点。

导出脚本使用版本化文件名且禁止覆盖。审看前后保留同一版本的文件。测试归档复跑时，另建目录，复制工程源码、锁文件和准备步骤生成的 `public/`、`src/fixture.json`，用 `npm ci` 恢复依赖，再从副本渲染。若跨系统保留生成物，复跑无需重新调用 macOS 的语音工具。
