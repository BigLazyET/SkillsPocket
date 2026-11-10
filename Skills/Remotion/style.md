# 风格

[入口](./SKILL.md) · [编排](./produce-prompt.md) · [工作流](./workflow.md) · [准备](./preparation.md) · [脚本](./script.md) · [音色](./tone.md) · [风格](./style.md) · [素材](./resources.md) · [音效](./sfx.md) · [质量门](./quality.md)

本文件规定一支片子怎么锁样式。名单和「未逐个实测」以 [Video.md](../Video.md) 的风格一节为准。镜头工具在 [workflow.md](./workflow.md) 的「画面」，不在这里按仓库排队。

核对日期：2026-11-10。

## 先锁自家样式

默认是一套为了看清楚的样式：统一的背景、统一的字体、统一的信息层级。转场帮助这句话被看懂。Video.md 的 Remotion 一节已经这样写：先做初版，再补约束，不预先叠满风格 Skills。

系列片已经锁过背景、字体和动画密度时，先复用。没有时，在准备结论里写明这套自家样式，连同建议的画幅和字体。用户否定再改。

五秒初剪是第一次把这套样式交出去看的成片画面。窗口、成品旁白和核对过的 SRT 按 [workflow.md](./workflow.md) 的「五秒初剪」。主人看样式、字体、动画，以及画面是否对上简报。他指出问题，只改那些地方，再渲染这约 5 秒。没接受之前不铺全片，也不锁定短样片。

接受之后，背景、字体和动画密度沿用到后面。要改这套样子，先问。长于约 1～2 分钟的片子，再用短样片看这套样子在更长的一段里是否还成立。短样片不代替五秒初剪。不长于这个长度的片子不再另做短样片。没有成品音轨和核对过的 SRT，不做这版初剪。

## 何时才打开第三方风格仓库

简报确实需要那种样子时才打开一个：白板、手绘、火柴人、用户点名的画廊方向，或其他他指定的参考。一次只打开这一个。不要按 Video.md 风格一节的列出顺序自动往下试，也不要因为 sy-style-100 排在第一就拿它当默认。

有参考时写清四件事：学哪一段、配色、构图、运动逻辑。不要只写「照着做」。

打开之前核对它是不是 Remotion、本机能否跑、产物能否接进当前工程。代码动画彼此技术相近，并不等于能直接接上。对不上或跑不起来：说明原因，问用户换参考或回到自家样式。不自动改开清单里的下一个。

五秒初剪接受之后要换样子，先问。

## 清单里的资源

用法和许可以各仓库当前 README 为准。下表是对照，不是尝试顺序。

| 资源 | 什么时候才打开 |
|---|---|
| [sy-style-100](https://github.com/xiaoxiong20xx-code/sy-style-100) | 用户点了它，或参考明确对上其中一种 |
| [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 用户要看画廊里的某一方向 |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 用户要把画风和讲解语法分开选 |
| [vox-director](https://github.com/Alisa0808/vox-director) | 可能依赖 Atlas API，可能收费。用户同意费用或云端之后才打开 |
| [srt-whiteboard](https://github.com/geeklee/srt-whiteboard-animation) | 片子要白板或手绘节奏去贴旁白 |
| [sweety-handdraw](https://github.com/threerocks/sweety-handdraw-video) | 片子要手绘线条和揭示 |
| [stickman-video-director](https://github.com/kaomei/stickman-video-director) | 片子要用火柴人的动作解释观点 |
| [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | 15 支带提示词和源码的短片，不是可安装 Skill。按 README 阅读。不要把 `skills add` 当成它已安装 |

[LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) 在 Video.md 里是审美层。只有简报明确要它时才打开。

Video.md 写明这些风格资源作者没有逐个实测。同一页的 Remotion 一节写明社区方案没有足够比较证据称为最优组合。本阶段不给这些资源排名次。

标题、字幕、片尾若要沿用模板组件，读 Video.md 的模板一节，只拿能接上的部分。

## 记在路径里

`production/paths.md` 写上实际用的是自家样式，还是哪一个仓库。付费、云端、许可不清的资源不自动换上。
