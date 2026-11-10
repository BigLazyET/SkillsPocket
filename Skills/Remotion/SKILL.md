---
name: remotion-personal-video
description: >-
  Use when this owner wants a Remotion video: a product introduction (产品介绍 / 产品宣传),
  a talking-head or voiceover explainer (口播 / 独立口播), or a technical explainer (技术讲解).
  Read produce-prompt.md and workflow.md in this folder first, then open only the stage
  file that step names. Does not replace the official Remotion skills (`npx skills add remotion-dev/skills`).
---

# Remotion 个人视频

主人用 Remotion 做产品介绍、独立口播和技术讲解时使用本 Skill。它规定阶段顺序、确认门和每阶段去读哪份规约。Remotion 的组件、预览和渲染写法以官方 Skill 为准，不在本目录里实现。

## 先读

1. [produce-prompt.md](./produce-prompt.md) — 编排提示词。按它做完一支片子。
2. [workflow.md](./workflow.md) — 只看顺序、交接物和何时停下。

然后按这两份文件点名的阶段，打开对应规约。[script.md](./script.md)、[tone.md](./tone.md)、[resources.md](./resources.md)、[sfx.md](./sfx.md)、[quality.md](./quality.md) 是各阶段的依据。不要把七份文件收成一段自由发挥的提示词。

## 不替代官方 Skill

Remotion 工程的创建、预览、渲染、字幕和动效，安装并遵守官方技能：

```bash
npx skills add remotion-dev/skills
```

安装命令、下载模型、删除和克隆声音之前先问用户。官方文档：[Remotion Skills](https://www.remotion.dev/docs/ai/skills)。

## 硬性停止

下面几件事没完成就不要进入下一项。细则在 [workflow.md](./workflow.md)。

- 分镜没有得到用户确认：不生成全长配音，不铺全片，不正式渲染。
- 样音没有通过：不合成全长旁白。
- 长片的短样片没有通过：不按该风格铺完全片。
- [quality.md](./quality.md) 的必过项没有通过：不正式导出。
- 当前会话不在主人的 Mac 上：不要连接 `127.0.0.1:3901`，也不要声称已经调用了 AudioSmith。改按 [tone.md](./tone.md) 说明环境并走降级。

## 和仓库里其他文档的关系

[Video.md](../Video.md) 是工具、素材和许可的清单，也是「无出镜 / 有出镜素材」声画分工的出处。[Remotion-AI-Video-Workflow.mmd](../Remotion-AI-Video-Workflow.mmd) 是同一意图的流程图。本目录把它们收成 Agent 能逐步执行的规约。

工具名单和许可以 Video.md 里已经写明的事实为准。阶段门以 workflow.md 为准。两处若对不上，停下来指出差异，不要另写一套流程。
