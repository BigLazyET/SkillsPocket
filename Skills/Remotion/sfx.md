# 音效

[入口](./SKILL.md) · [编排](./produce-prompt.md) · [工作流](./workflow.md) · [准备](./preparation.md) · [脚本](./script.md) · [音色](./tone.md) · [风格](./style.md) · [素材](./resources.md) · [音效](./sfx.md) · [质量门](./quality.md)

本文件规定音效和配乐怎么选、怎么对上 SRT、怎么限制音量。费用、规模和许可的表在 [Video.md](../Video.md) 第 2 节，这里不复制。进工程的 `<Audio>` 写法用官方 Remotion Skill。

核对日期：2026-11-10。费用、许可和「本地、无月度配额优先」见 Video.md 第 2 节。Video.md 第 1 节写明社区方案没有足够比较证据称为最优组合；本文件只写这一支片子的选用顺序。

## 输入和输出

输入是核对过的 `production/narration.srt`、短样片确定的画面，以及已有的个人音效库索引。没有这份 SRT 时，不给成片写切点。

输出是一份音效表，每条有：路径、听感、对应的 SRT 序号和起止、用途、时长、峰值大概落在哪里、来源、作者、许可、署名句子、实际使用的获取路径。配乐单独成行。

人听过之后，在该条写下「已听」以及是否使用。只有文件、没有这一句，不算完成。Agent 没有真正播放时，只能按文件名、标签和说明列出少量候选，并写明「尚未试听」。

## 谁来做音效设计

产品介绍的节拍和音效设计打开已安装的 video-shotcraft，跟随它的 sound design 做法。试听、许可和下面的降级仍以本文件为准。shotcraft 自带的音频在拷进 `public/sfx` 之前，按 Video.md 逐个文件核对许可。

口播讲解和技术讲解没有另一套自制的音效语法。选声音用下面的顺序，切点用 SRT。

## 降级顺序

怎么算这一条失败：文件不存在、命令报错、许可不适用于本片，或用户听过并否定。记下失败，试下一条，并写入 `production/paths.md`。商用片上的 CC BY-NC 直接跳过。许可不明的不进成片。付费库先问。可自动尝试的免费路径都没有合适的声音时，停下来问，不换到 Video.md 明确未纳入的月度文生音效。

1. 个人库里已经听过、许可仍适用的条目。索引列见 Video.md「建立个人音效库」。
2. [@remotion/sfx](https://www.remotion.dev/docs/sfx/)。加入命令先给用户看。
3. [earshot](https://github.com/Leonxlnx/earshot)。命令形状以它的 README 为准。Video.md 核对过的例子是 `earshot sfx render whoosh_fast/crisp -o whoosh.wav`。听感不对就换下一条；Video.md 记录过一次合成听感不佳，这不表示 earshot 不能用于合适的电子短音。
4. Kenney 的 CC0，以及 Freesound 上这一条的 CC0。Freesound 的 CC BY 要署名才用。
5. Mixkit、Pixabay。保存条目页面，不把它们写成统一的 CC0。
6. 产品介绍里，video-shotcraft 自带包中许可已经核对的那一条。
7. Envato 一类付费库：先问。不同意就停在没有这条音效的状态。

不把 ElevenLabs、SFXMint、Lots of Sounds 放进自动降级。Video.md 写明这是当前选型范围，不是那些产品没有免费层的结论。

## 什么时候出声

音效标记动作，不标记句子。候选的类别和文件名示例用 Video.md 的个人库表：whoosh、pop、click、typing、paper、riser。

旁白正在说关键词时，不叠一声会盖住字的音效。尾音不要拖进下一条 SRT 的关键词。配乐和音效分轨。旁白出现时把配乐降低。辅助录屏自带的解说保持静音。清单里写明要留的操作声，才作为音效轨的一条，并跟主旁白一起听。

## 音量和切点

- 主音轨是前景。整片响度的通过条件在 [quality.md](./quality.md)。
- 切点用 SRT 的起止和画面动作，不用「大概在这一段」，也不按字数估计。
- 改了主音轨或 SRT 之后，重对受影响的切点。
- 同一声在全片反复使用时，间隔开。

## 失败时

| 现象 | 处理 |
|---|---|
| 只有检索结果 | 停在候选，请用户听 |
| 音效盖过旁白 | 降音效或换更短的一条 |
| 许可是 NC 或不明 | 商用片拿掉。不明的不进成片 |
| shotcraft 的声音许可没核对 | 不拷进工程，改走上面的下一条 |

## 来源

选型、试听边界和个人库示例来自 [Video.md](../Video.md) 第 2 节。
