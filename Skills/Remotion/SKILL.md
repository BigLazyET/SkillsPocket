---
name: remotion-personal-video
description: >-
  Use when this owner wants a Remotion video: a product introduction (产品介绍 / 产品宣传),
  a talking-head or voiceover explainer (口播 / 独立口播), or a technical explainer (技术讲解).
  Read produce-prompt.md and workflow.md first. Run preparation.md before any other stage
  and confirm form A, B, or C. Timing comes from a finished-audio SRT. Official Remotion
  skills (`npx skills add remotion-dev/skills`) implement typography, layout, motion,
  captions, and render. video-shotcraft and video-talkcraft are preferred when installed
  and a good fit, not required dependencies.
---

# Remotion 个人视频

主人用 Remotion 做产品介绍、独立口播和技术讲解时使用本 Skill。它规定阶段顺序、确认门和每阶段去读哪份规约。排版、布局、运动、字幕和渲染以官方 Skill 为准。video-shotcraft 和 video-talkcraft 是合用时优先打开的社区 Skill，不是本 Skill 的身份，也不是开工依赖。

## 先读

1. [produce-prompt.md](./produce-prompt.md) — 编排提示词。按它做完一支片子。
2. [workflow.md](./workflow.md) — 只看顺序、交接物和何时停下。

第一阶段是 [preparation.md](./preparation.md)。硬停没解除时，不配音、不铺画面。建议项写明即可。通过之后，只打开 workflow 点名的那一份。

[script.md](./script.md)、[tone.md](./tone.md)、[style.md](./style.md)、[resources.md](./resources.md)、[sfx.md](./sfx.md)、[quality.md](./quality.md) 是各阶段的依据。不要把这些文件收成一段自由发挥的提示词。

## 官方 Skill 与社区 Skill

官方技能负责创建、markup、Studio、渲染、字幕：

```bash
npx skills add remotion-dev/skills
```

已安装且合用时，产品界面和宣传节奏优先打开 [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)，口播驱动的讲解和出镜布局优先打开 [video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft)。没装、不合用或只覆盖一部分时，用官方 skills 和清单里的真实素材做其余部分。不要把这两个仓库复制进 SkillsPocket。选择规则在 [workflow.md](./workflow.md) 的「画面」。

安装、下载模型、删除、克隆和正式导出之前先问用户。预览和短样片在本轮已经同意过一次之后可以继续。官方文档：[Remotion Skills](https://www.remotion.dev/docs/ai/skills)。

社区 Skill 的步骤若和本 Skill 的门冲突，以 [workflow.md](./workflow.md) 的「社区 Skill 与这些门冲突时」为准。

## 硬性停止

细则在 [workflow.md](./workflow.md) 和 [preparation.md](./preparation.md)。

- 形态 A、B、C 两可或互相冲突：不配音、不铺画面。
- 继续做会编出产品、经历、媒体，或会用许可不清的素材：停下问。
- 形态 C 的稿没确认，或样音没通过：不合成全长旁白。
- 没有从成品音轨核对过的 SRT：不铺全片，不正式导出。
- 长片的短样片没有通过：不按该样式铺完全片。
- [quality.md](./quality.md) 的必过项没有通过：不正式导出。
- 当前会话不在主人的 Mac 上：不要连接 `127.0.0.1:3901`，也不要声称已经调用了 AudioSmith。改按 [tone.md](./tone.md) 说明环境并询问降级。

社区 Skill 没装，不是硬停。

## 和仓库里其他文档的关系

[Video.md](../Video.md) 是工具、素材和许可的清单。阶段里需要的技能和工具从那里打开，不在本目录重写一份名单。[Remotion-AI-Video-Workflow.mmd](../Remotion-AI-Video-Workflow.mmd) 是同一流程的图。图和 workflow.md 不一致时，以 workflow.md 为准，不要为此停下。

工具名单和许可以 Video.md 里已经写明的事实为准。阶段门以 workflow.md 为准。两处若对不上，在回复里指出差异，按这两条做，不要另写一套流程，也不要停掉这一轮。
