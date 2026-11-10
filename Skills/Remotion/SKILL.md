---
name: remotion-personal-video
description: >-
  Use when this owner wants a Remotion video: a product introduction (产品介绍 / 产品宣传),
  a talking-head or voiceover explainer (口播 / 独立口播), or a technical explainer (技术讲解).
  Read produce-prompt.md and workflow.md first. Run preparation.md before any other stage:
  confirm form A, B, or C and stop if prerequisites are missing. Does not replace the
  official Remotion skills (`npx skills add remotion-dev/skills`).
---

# Remotion 个人视频

主人用 Remotion 做产品介绍、独立口播和技术讲解时使用本 Skill。它规定阶段顺序、确认门和每阶段去读哪份规约。Remotion 的组件、预览和渲染写法以官方 Skill 为准，不在本目录里实现。

## 先读

1. [produce-prompt.md](./produce-prompt.md) — 编排提示词。按它做完一支片子。
2. [workflow.md](./workflow.md) — 只看顺序、交接物和何时停下。

第一阶段是 [preparation.md](./preparation.md)。准备没通过时，不要打开脚本、音色或素材去做成片。通过之后，只打开 workflow 点名的那一份。

[script.md](./script.md)、[tone.md](./tone.md)、[resources.md](./resources.md)、[sfx.md](./sfx.md)、[quality.md](./quality.md) 是各阶段的依据。不要把这些文件收成一段自由发挥的提示词。

## 不替代官方 Skill

Remotion 工程的创建、预览、渲染、字幕和动效，安装并遵守官方技能：

```bash
npx skills add remotion-dev/skills
```

安装命令、下载模型、删除和克隆声音之前先问用户。官方文档：[Remotion Skills](https://www.remotion.dev/docs/ai/skills)。

## 硬性停止

下面几件事没完成就不要进入下一项。细则在 [workflow.md](./workflow.md) 和 [preparation.md](./preparation.md)。

- 准备没通过，或形态还不是 A、B、C 里确认过的一种：不写脚本、不配音、不铺画面。
- 条件不够：立刻问用户。不编造产品、音色、画幅、镜头清单或缺失的媒体。
- 形态 C 的稿没确认，或样音没通过：不合成全长旁白。
- 没有核对过的主语音时间轴：不铺全片，不正式导出。
- 长片的短样片没有通过：不按该风格铺完全片。
- [quality.md](./quality.md) 的必过项没有通过：不正式导出。
- 当前会话不在主人的 Mac 上：不要连接 `127.0.0.1:3901`，也不要声称已经调用了 AudioSmith。改按 [tone.md](./tone.md) 说明环境并询问降级。

## 和仓库里其他文档的关系

[Video.md](../Video.md) 是工具、素材和许可的清单，也是「主音轨只留一份」的出处。[Remotion-AI-Video-Workflow.mmd](../Remotion-AI-Video-Workflow.mmd) 是较早的两条分支图。本目录把执行收成准备阶段加三种形态。

工具名单和许可以 Video.md 里已经写明的事实为准。阶段门以 workflow.md 为准。两处若对不上，停下来指出差异，不要另写一套流程。
