---
name: remotion-personal-video
description: >
  用 Remotion 制作或修改个人产品介绍、真人出镜视频、口播和技术讲解。
  适用于根据主题、调研和已有素材起草逐镜脚本，以及制作字幕、样片和可编辑成片。
---

# Remotion 个人视频

先读 [workflow.md](./workflow.md)，按任务范围进入对应阶段。新片从 [preparation.md](./preparation.md) 开始。续做时从最早失效的交接物恢复，沿用仍有效的用户决定和预览同意。

音画同步是核心规则。成品音轨定时间，SRT 定位讲到哪一段，分镜定素材和表达意图，实际发音与画面动作定精确落点。AI 可以补充分镜留白处的编排，具体规则见 [timeline.md](./timeline.md)。A/B 需要新录或补录时，AI 从逐镜制作稿另出一份可直接读的录制稿，见 [script.md](./script.md#给录制者的口播稿)。

- 准备和建项见 [preparation.md](./preparation.md)。AI 编剧、音色、时间映射和单行字幕见 [script.md](./script.md)、[tone.md](./tone.md)、[timeline.md](./timeline.md) 和 [captions.md](./captions.md)。
- 画面与声音见 [style.md](./style.md)、[resources.md](./resources.md)、[sfx.md](./sfx.md)。验收和导出见 [quality.md](./quality.md)。
- Remotion 的组件与命令以 [官方 Remotion Skills](https://www.remotion.dev/docs/ai/skills) 为准。已安装时直接使用。缺少且任务需要时，在得到安装同意后运行 `npx skills add remotion-dev/skills`。按镜头选用合适的社区 Skill，选择和冲突规则见工作流。
- 辅助素材优先复用当前 Skill 和工程里合用的资源。用户自备的通用素材可补位或改善效果，开工无需先备齐。选材顺序与真实演示的要求见 [resources.md](./resources.md#通用素材的选用顺序)。
- [Video.md](../Video.md) 是工具和素材来源清单，使用时核对实际版本及条款。[流程图](../Remotion-AI-Video-Workflow.mmd) 供浏览，阶段顺序以工作流为准。

从 SkillsPocket 检出目录使用此 Skill。它会读取相邻的 `Video.md`，部分任务还会用到仓库内的像素动效 Skill。安装到 Agent 的技能目录时，可在宿主支持且会解析到原目录的情况下使用链接，保留仓库依赖。单独复制此文件夹时需一并保留这些引用的相对布局。
