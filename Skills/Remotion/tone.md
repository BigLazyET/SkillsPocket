# 音色

[入口](./SKILL.md) · [编排](./produce-prompt.md) · [工作流](./workflow.md) · [准备](./preparation.md) · [脚本](./script.md) · [音色](./tone.md) · [风格](./style.md) · [素材](./resources.md) · [音效](./sfx.md) · [质量门](./quality.md)

本文件规定主音轨怎么选定、怎么调用，以及 SRT 怎么从成品音轨得到。它不包含 Remotion 组件，也不把某种音色写成仓库里的配置。形态以 [preparation.md](./preparation.md) 已确认的为准。出镜镜头的形状、位置和运动记在 [script.md](./script.md)。

核对日期：2026-11-10。AudioSmith 的工具名和内存要求对应该日上游 README 与 `docs/local-api.md` 中的 0.5.0-beta.1。本机安装的版本不同时，以本机应用为准。

语音工具的总清单在 [Video.md](../Video.md) 第 3 节。SRT 的含义以该页「SRT 是配音与画面的时间依据」为准：逐字稿定义说什么，成品音轨定义何时说，SRT 记录序号、起止和文本。Video.md 把 VoiceStudio 与 AudioSmith 都列为本地工作台，并写明未逐项实测。本文件在主人的 Mac 上默认走 AudioSmith，这不改写那份清单的排名。

## 按已确认的形态

准备阶段没写明 A、B 或 C 时，回到 [preparation.md](./preparation.md)。

| 形态 | 主音轨 | SRT | 不做什么 |
|---|---|---|---|
| A 真人出镜视频 | 与画面一致的那条人声 | 识别该成片的音轨 | 不另做 TTS，不为对口型分析嘴型，不叠第二条讲解 |
| B 真人讲解音频 | 用户给出的讲解 | 识别音频文件，或识别那条视频的音轨 | 不把画面布局成出镜表演，不用 TTS 替换人声 |
| C 没有真人只有脚本 | 指定音色的 TTS | 合成结果再对齐 | 稿未确认、样音未通过时不做全长 |

A、B 的文件若用户说还不是要用的那一条，停下来问他交哪一版。不自行决定剪掉哪些口误。video-talkcraft 若要求先剪口水词，先把报告给用户看；他同意之后才改文件。

主音轨若从视频里抽出来单独铺，视频自带的音轨必须静音，并且起点一致。两条都留着会双声。保留视频原声、不再另铺一份，也可以。两种只选一种。

降噪、均衡、压缩只在用户要求时做。

## SRT

三种形态都交出 `production/narration.srt`。字幕、画面和音效引用它的序号和起止。真人录音也要有这份文件。来源说明写在 `production/narration-srt.md`：形态、源文件路径、实际使用的识别或合成路径。两份都放在视频工程里，不写进 SkillsPocket。

一份合格的 SRT：

- 覆盖从第一句人声到最后一句。没说出口的句子不在里面。
- 每一条有序号、起止时间和实际听到或合成出来的词。
- 条与条不重叠，除非真的有两个人同时说话；那种情况要标明。
- 起止来自这条成品音轨的识别或对齐。只有稿子时的秒数是估计，不能写入这个文件。
- 稿子只用来改人名、术语、英文品牌和同音字。

核对：用同一条音轨听开头、中段、结尾和最长的一处停顿。文本与声音不一致就改文本或重跑识别。断句、大约 8～18 个汉字的示例宽度，以及官方 [parseSrt()](https://www.remotion.dev/docs/captions/parse-srt) 只负责解析，都见 Video.md 的 SRT 一节。句级 SRT 不是逐字高亮。词级时间必须落在所属条目的起止之内，并且不另做一份计时文件。

画面上的字幕是这份 SRT 的换行。为了留画面而加的停顿，要写回音轨和 SRT。

解析和绘制用官方 `remotion-captions`。解析不证明已经和声音核对过。

### 识别的降级顺序

用于 A、B，以及核对 C 的合成草稿。把每次失败和实际使用的路径写入 `production/paths.md`。

怎么算失败：工具不在本机、命令非零退出、结果是空的、或起止盖不住这段人声。专名听错不是换工具的理由，用稿子校对。

1. 会话在主人的 Mac 上且 AudioSmith 有响应：`transcribe`。文件必须真的交给它。
2. 识别工具读不了这个容器：用 Video.md 第 7 节的 FFmpeg 抽出音轨，再把抽出的文件送回同一步。具体参数以本机文档为准。Video.md 写明那些命令没有在清单里核对过，这里不补一套未核对的参数。
3. 上一步缺失或报错：whisper.cpp 运行 Whisper `large-v3-turbo`，这是 Video.md 记录的本地路径。
4. 用户已经在本轮指定另一个当前会话能调用的本地模型：用他指定的那个。
5. 飞书妙记、剪映是 Video.md 转述的云端或应用内转写。不自动使用。本地路径都失败后停下来问；他同意才用。
6. 上面都失败：停下来问。不按稿子填写起止，也不改用 TTS 冒充 A、B 的声音。

### C：合成之后再对齐

全长合成的门见下文。合成出的 WAV 或 M4A 才是主音轨。SRT 用这次音轨的对齐结果。AudioSmith 导出的字幕、Edge TTS 的 `--write-subtitles` 都只是草稿，仍走上一节的识别顺序核对。

没有这条成品音轨时，不写 `narration.srt`。

## 配音的降级顺序

只用于形态 C。A、B 的识别失败不改走这条。换音色是用户听得到的变化，除了第 1 步以外都要先问。问过并同意的那一条失败后，再问，不自行改去下一条。

1. 主人的 Mac 上 AudioSmith 有响应：按下文做样音，通过后 `generate_speech`。
2. 人在那台 Mac 上但 health 没有响应：说明结果，请用户打开应用。仍然没有响应，停下来问他换机器，或是否同意 Edge TTS。
3. 会话不在那台 Mac 上：不连接 `127.0.0.1`。问他换机器，或是否同意 Edge TTS。
4. 用户点名 Video.md 第 3 节里的 VoiceStudio、GPT-SoVITS、VoxCPM2 或 IndexTTS：用他点名的那一个，并先说明该项目的部署和许可还要按所用版本核对。不逐个自动试。
5. 用户同意之后才用文末的 Edge TTS。它失败就停下来问。

怎么算 AudioSmith 合成失败：health 不通、工具报错，或任务失败。读错专名时改正文再出样音，不换引擎。

## 送进语音工具的文本

只用于形态 C。A、B 不把稿子送进 TTS。

从制作脚本里抽出要念的正文。屏幕文字、素材备注、「仅屏幕展示」和段落标题都不送。

不要假定 TTS 会自动忽略【旁白】之类的自定义标记。先得到一份纯正文，再调用。

AudioSmith 自己的控制标记可以留在这份正文里：`[pause 400ms]`、`[slow]`、`[fast]`，以及读音 `[[词|读法]]`。这些标记不是给观众看的字幕文本。写入 SRT 时用听众听到的词。

没有特殊标记的句子保持制作脚本的原文，方便校对。

## AudioSmith

形态 C 的合成首选它。A、B 只在这台 Mac 上用它做 `transcribe`，不用它替换真人声音。它是跑在 Apple Silicon Mac 上的本地语音工作室：<https://github.com/hehehai/AudioSmith>。模型在本机。它不是本仓库的代码，也不要把它的密钥写进 SkillsPocket。

### 什么时候叫得到

同时满足才调用：

- 当前会话就在主人的那台 Mac 上，应用已打开。
- 本地 API 开着。默认基址是 `http://127.0.0.1:3901`。端口以应用设置为准。只在已经确定是这台 Mac 时，才用 `GET /health` 看它是否在听。

远程、云端或其他电脑上的 Agent 够不到使用者的 `127.0.0.1`。这种会话不要发起连接，不要把失败说成应用损坏，直接按上面的降级询问用户。

应用在本机但没有响应时，说明 health 检查的结果，请用户打开应用。不要改口声称已经合成成功。

### 接入

在运行中的应用里打开 Developers → Connect your agent，或 Integrations，生成 Cursor 的配置。把生成结果合并进 `~/.cursor/mcp.json`，保留文件里其他服务。不要手写一份猜测的 JSON 覆盖原文件。

应用同时提供：

- 第一方 MCP，不是商店插件。Streamable HTTP 在 `http://127.0.0.1:3901/mcp`。stdio 为应用二进制 `AudioSmith --mcp-stdio`（应用包内路径是 `AudioSmith.app/Contents/MacOS/AudioSmith --mcp-stdio`）。stdio 只是转到已经在跑的应用。
- OpenAI 兼容 API：`http://127.0.0.1:3901/v1`。
- 原生 API：同一主机上的 `/api`。

Agent 走 MCP。不要为了绕过 MCP 去猜未在本文件列出的请求体。

应用还会生成它自己的 Skill，装到 `~/.cursor/skills/audiosmith/`。那份 Skill 管每个工具的参数。本文件管视频流程里何时调用。两份都在时，参数以应用生成的那份为准，阶段门仍以 [workflow.md](./workflow.md) 为准。安装前告诉用户。

生成的配置可能含密钥。密钥留在本机配置或钥匙串里，不写入视频工程和本仓库。

### 与本流程有关的工具

| 工具 | 用途 | 约束 |
|---|---|---|
| `list_voices` | 看已有音色 | 已有合适音色就不要重新设计 |
| `design_voice_candidates` | 按一句中文或英文描述生成候选 | 候选给用户听，由用户选 |
| `design_voice` | 把选中的候选存成音色 | 使用用户选的那一次 |
| `clone_voice` | 用一段录音做克隆 | 调用参数里要有明确同意（`consent: true`）。只克隆用户本人或他已获授权的录音 |
| `generate_speech` | 形态 C 的全长旁白 | 稿已确认，且样音已通过。A、B 不调用 |
| `transcribe` | 从成品音轨得到 SRT，或核对 TTS 草稿 | 专名只按听到的声音修正。不把没念的句子写进去 |
| `get_job`、`cancel_job` | 查看或取消长任务 | 长合成用任务状态，不要假设调用立刻结束 |
| `download_model` | 下载缺的模型 | 必须带确认（`confirm: true`），且先得到用户同意 |
| `delete_item` | 删除音色等 | 同样要确认参数和用户同意 |

克隆和设计只在这台 Mac 上、或持有 API key 时可用。没有同意就不调用 `clone_voice`。

### 设计音色

用大白话描述感觉，例如「沉稳的男声」「亲切自然的女声」。用户不必记住音色 ID。描述使用中文或英文。

对应模型是 Qwen3-TTS 1.7B VoiceDesign，许可证 Apache-2.0。它在 Quality 包里，上游写明大约需要 24 GB 内存。包未下载时，先告诉用户体量（上游把 Quality 包写成约 13.4 GB，中文内容约 14.9 GB）再询问，同意后才 `download_model`。

先 `design_voice_candidates`，把候选放给用户选。选定后用该候选的 seed 调用 `design_voice`。不要替用户选定并直接合成全长。

设计出来的音色若以后转成克隆音色，听感接近，不会相同。需要转换时先告诉用户这一点。

### 克隆

两条模型，都要事先同意：

- 快：Qwen3-TTS 0.6B Base。
- 高保真：Qwen3-TTS 1.7B Base。

用用户指定的参考录音。参考录音的许可和使用范围按 Video.md：本人或已获授权。不要用别人的公开视频声音来克隆。

### 样音和全长

只用于形态 C。

样音内容：这支片子里的术语、一处中英混读、一个较长的句子。请用户听读音、漏字、语气、语速和停顿。

通过之后才 `generate_speech` 全长旁白。导出 WAV 或 M4A 作为主音轨，再按上文写成 `production/narration.srt`。应用能把响度做到 −16、−18 或 −23 LUFS，并能裁掉首尾静音。选哪一档响度记进成片记录，判断标准在 [quality.md](./quality.md)。导出附带的字幕只是草稿。

商用片子不要默认 OmniVoice。上游模型表把它标为 CC BY-NC 4.0。商业向的默认保持在 Apache-2.0 的 Qwen3-TTS 路径上，除非用户另行确认许可。

## 降级：Edge TTS

只用于形态 C，并且只在用户同意之后。它不是设计音色，也不是克隆。

Edge TTS 指 [rany2/edge-tts](https://github.com/rany2/edge-tts) 这个命令行，调用微软 Edge 的在线神经语音。

- 只有预设音色。用 `--list-voices` 列出，向用户说明几个中文候选的特点，让他选 ShortName。
- 需要网络。
- 语速和音量用 `--rate`、`--volume`。负值要写成 `--rate=-10%`。
- 自定义 SSML 已从该工具移除（上游写明自 5.0.0 起不再接受任意 SSML）。
- `--pitch` 在上游 README 里仍有说明，PyPI 6.1.8 则写明 6.0.3 起该参数不再有效。调用前看本机 `edge-tts --help`。
- `--write-media` 写出音频，`--write-subtitles` 写出字幕草稿。草稿仍要按识别顺序核对。
- 安装（`pipx install edge-tts` 或 `pip install edge-tts`）先问用户。
- 该客户端和微软服务的商用许可本仓库没有核完。简报若是商用，要告诉用户这一点。不要宣称 Edge TTS 已经授予商用权。

Smartpigai 文章里的搭建示例写的是 Edge TTS。那是文章的做法。主人本机 AudioSmith 可用时，不用那一条做默认。

## 失败时

| 现象 | 处理 |
|---|---|
| 形态还没确认 | 回到 [preparation.md](./preparation.md) |
| 不在主人的 Mac 上 | 停止调用 127.0.0.1，按配音降级询问。不自动换音色 |
| A、B 的本地识别都失败 | 停下问。不编起止，不改用 TTS |
| 模型未下载 | 报出工具返回的缺口和体量，等用户同意再下载 |
| 样音读错专名 | 改纯正文后重新出样音 |
| 全长或人声改了某一句 | 替换受影响的音频，重做 SRT 和后续画面。不保留新旧两段叠在一起 |
| 克隆没有同意 | 不调用 |

## 来源

工具分层和 SRT 规则来自 [Video.md](../Video.md) 第 3 节。形态 C 先确认稿再配音、用感觉描述声音，来自 [Smartpigai 的文章](https://x.com/Smartpigai/article/2073753428212478384)。AudioSmith 的地址、端口和工具名来自其仓库 README 与 `docs/local-api.md`。Edge TTS 的行为来自 rany2/edge-tts 的 README 与 PyPI 6.1.8 说明。
