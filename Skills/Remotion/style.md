# 风格

[入口](./SKILL.md) · [编排](./produce-prompt.md) · [工作流](./workflow.md) · [准备](./preparation.md) · [脚本](./script.md) · [音色](./tone.md) · [风格](./style.md) · [素材](./resources.md) · [音效](./sfx.md) · [质量门](./quality.md)

本文件规定一支片子怎么选定一种视觉风格、怎么写参考、怎么用短样片锁定。名单、链接和「未逐个实测」以 [Video.md](../Video.md) 的风格一节为准，这里不另排优劣。镜头配方不在这里写，画面阶段打开已安装的 video-shotcraft 或 video-talkcraft。

核对日期：2026-11-10。

## 何时做

叙事意图已经写进制作脚本之后就可以做风格简报。短样片用来锁定，而短样片要有成品音轨和核对过的 SRT，所以锁定落在画面阶段，不在只有稿子的时候。

一次只打开一种风格资源。不要把这一节的仓库一次性装上。Video.md 的 Remotion 一节写过：先做初版，再补约束，不预先叠满风格 Skills。

## 简报

先定叙事和要的样子，再检查这套东西是不是 Remotion、本机能否跑、产物能否接进当前工程。代码动画彼此技术相近，并不等于能直接接上。

有参考时写清四件事：学哪一段、配色、构图、运动逻辑。不要只写「照着做」，也不要靠抽帧去猜。

没有参考时，用短样片让人看见偏好。Video.md 写明这些风格资源作者没有逐个实测。同一页的 Remotion 一节写明社区方案没有足够比较证据称为最优组合。本阶段不给这些资源排名次，只决定这一支片子打开哪一个。

## 清单里的资源

用法和许可以各仓库当前 README 为准。下表只说明本阶段怎么对待它们。

| 资源 | 本阶段怎么用 |
|---|---|
| [sy-style-100](https://github.com/xiaoxiong20xx-code/sy-style-100) | 用户点了它，或短样片锁定前它是第一个能跑的 Remotion 风格 |
| [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 先看画廊里的样片，再决定学哪一种方向 |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 画风和讲解语法可以分开选 |
| [vox-director](https://github.com/Alisa0808/vox-director) | 可能依赖 Atlas API，可能收费。不自动换到它 |
| [srt-whiteboard](https://github.com/geeklee/srt-whiteboard-animation) | 看绘制节奏能否贴上旁白的 SRT |
| [sweety-handdraw](https://github.com/threerocks/sweety-handdraw-video) | 先看线条、揭示方式和文字是否读得清 |
| [stickman-video-director](https://github.com/kaomei/stickman-video-director) | 用角色动作解释观点时再打开 |
| [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | 15 支带提示词和源码的短片，不是可安装 Skill。按 README 阅读和复用，不要把 `skills add` 的成功当成它已安装 |

[LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) 在 Video.md 里是审美层，不是产品片或口播片的镜头 Skill。只有风格简报明确要它时才打开。

## 短样片锁定

长片先做约 1～2 分钟，里面要有成品旁白、SRT 字幕、至少一处真实素材，以及这一种风格的配色、字体和动画密度。用户接受之后，全片沿用这些，不在后面的章节再换一套。片子本身不长于这个长度时，第一版整片就是样片，仍要人看过。

系列片复用已经锁定的背景、字体和动画密度。标题、字幕、片尾若要沿用模板组件，读 Video.md 的模板一节，只拿能接上的部分，不整包叠上。

## 降级顺序

把试过的路径写入 `production/paths.md`。

1. 用户点名的那一个。先核对它是不是 Remotion、本机能否跑、产物能否接进工程。
2. 它缺失、报错，或底层不是 Remotion：短样片还没锁定时，按 Video.md 风格一节的列出顺序试下一个能跑的 Remotion 资源，并写明换过。跳过 vox-director，除非用户已经同意它的费用或云端依赖。mg-styles-15 只当资料读，不算安装成功。
3. 短样片已经锁定：不再自动换样子。修当前这一个；修不好就停下来问。
4. 用户坚持的参考无法接入 Remotion：停下来说明，等他改参考或同意换一个能跑的。

付费、云端、许可不清的资源不在自动换的范围内。全部可自动尝试的资源都失败时，停下来问，不现场发明一套画风。
