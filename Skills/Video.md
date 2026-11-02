# Video：个人视频素材与 Skills

[项目首页](../README.md) · [Game 清单](Game.md)

聚焦个人视频从素材、动效、配音、音效到成片的制作。外部链接不代表已安装；仓库的 MIT 许可不替代外部工具、模型和素材自身的许可。核对日期：2026-11-02；选型建议需结合样片、硬件和实际制作需求验证。

本次补充来源：言说新事《一条讲解视频的制作全流程拆解》，[原视频](https://v.douyin.com/6aGcjaWCRz4/)（[固定地址](https://www.douyin.com/video/7703213715362158075)），2026-11-01 发布，时长约 12:15。依据用户提供的本地 `Remotion.mp4` 全片音轨转写，并对照关键画面及字幕核对；下文用时间段标注视频内容，另将操作建议和上游核实结果明确区分。视频中的社区方案未被作者逐项实测，不能把展示样片等同于本项目实测。

## 导航

- [Remotion 与社区制作 Skills](#remotion)
- [SFX 音效](#sfx)
- [语音工作室、配音与 SRT 同步](#voice)
- [风格](#styles)
- [视频模板](#templates)
- [表情、品牌、图标与可复用角色素材](#icons)
- [官方 Skills 与制作环节补充](#production)
- [个人发布工作流](#workflow)

<a id="remotion"></a>

## 1. Remotion 做视频和动态图形

用 React 创建视频和动态图形，偏向于产品宣传，口播讲解，技术讲解等视频

可用 Remotion 官方维护的 remotion-dev/skills 打底；宣传片可评估社区 video-shotcraft，口播讲解可评估 video-talkcraft，动效设计可参考 motion-design-skill。社区方案按样片、依赖和项目需求选择，目前没有足够的比较证据将这些方案称为“最优组合”。

- 官方地址：[Remotion Skills](https://www.remotion.dev/docs/ai/skills)
- 社区产品宣传片候选：[video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) 
- 社区口播讲解片候选：[video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft)
- 社区审美层：[LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)


### 从工具选择到动画制作（视频 00:12–01:02、06:56–08:14）

- **先做初版，再补约束**：作者先用 Remotion 官方 Skill 和必要素材跑通初版，发现问题再加约束，不预先叠满风格 Skills。这是创作习惯，不意味着跳过环境检查、必讲内容或交付规格。
- **以讲清楚为目标**：背景、字体和信息层级先统一；转场、卡片移动、角色动作应服务讲解，避免每个元素都飞入飞出。
- **用短样片确定风格**：长片先做约 1～2 分钟，确认配色、字体、节奏、动画密度及素材使用，再扩展到全片。作者一次完成 16 分钟视频是个例，不作为默认流程。
- **分清职责**：模型负责理解与设计，Agent 负责调用工具，Remotion 负责渲染；脚本、素材、录音、音效不绑定某个模型。作者的模型审美与写作偏好属于个人体验，不作为通用排名。

用于下达任务的整理建议：给出讲解目标、最终音轨、SRT、逐字稿、素材目录、字体/背景与不可遗漏项，先交付短片预览，再按反馈继续。脚本细节见[个人发布工作流](#workflow)。

<a id="sfx"></a>

## 2. SFX 音效(Sound Effects)

补充 `@remotion/sfx` 的音效来源，包括代码合成与现成素材库：earshot 支持代码合成，Kenney/Freesound 等提供素材，不能统一视为代码生成。


| 方案 | 费用 | 规模/特点 | 怎么进 Remotion | 适合 |
|---|---|---|---|---|
| [@remotion/sfx](https://www.remotion.dev/docs/sfx/) | 免费 | whoosh/whip、UI 点击等；目录随版本变化 | `import` 直接用 | 起步转场 |
| [earshot](https://github.com/Leonxlnx/earshot) | 开源免费 | 上游标称 252 个代码合成音效（2026-11-02 核对）；可 `kit`/`describe` | `earshot sfx render ID -o sound.wav` → WAV → `<Audio>` / `staticFile` | 主补库、切点对齐、Agent 听感 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) 自带包 | 代码开源；音频许可逐项确认 | 含音效与配乐工作流；素材数量与各文件许可待核实 | Skill/流水线内嵌，或拷到 `public/sfx` | 产品宣传片一站式 |
| [Kenney](https://kenney.nl/assets?q=audio) | CC0 免费 | 游戏/UI 音效包，量大 | 下 WAV → `public/sfx` | 点击、UI、通用短音 |
| [Freesound](https://freesound.org)（选 CC0） | 免费（需选许可证） | 海量真人录音 | 下 WAV → `public/sfx` | 真实质感、冷门声 |
| [SoundCN](https://github.com/kapishdima/soundcn) / [soundcn.xyz](https://soundcn.xyz) | 上游代码与音频许可待逐项核实 | UI 点击类 | 导出文件再挂 `<Audio>` | 网页式交互音 |
| [Mixkit 音效](https://mixkit.co/free-sound-effects/) | 免费，按 [SFX 许可](https://mixkit.co/license/)使用 | 转场、UI、环境等音效；其他素材类别的许可分别看 | 下载 → `public/sfx` → 音频轨 | 常用成品音效补充；视频 11:15 左右推荐 |
| [Pixabay 音效](https://pixabay.com/sound-effects/) | 免费，适用 [Content License](https://pixabay.com/service/license-summary/) | 多类音效，不统一标为 CC0；不等于可原样再分发 | 下载并保存条目来源 → 音频轨 | 常用音效补充；视频 11:21 左右推荐 |
| [Envato Elements](https://elements.envato.com/sound-effects) | 订阅付费，按项目许可使用 | 商业素材库，保留作付费备选 | 下载授权素材 → 音频轨 | 免费库未找到合适音效时；非默认免费栈 |

**当前选型范围**：保留本地、无月度生成配额优先的偏好，暂不纳入 ElevenLabs、SFXMint、Lots of Sounds 及依赖月度额度的文生音效服务；这不代表这些产品没有免费层或不支持商用，其当前价格与条款尚未逐项核实。

**本地与免费素材优先的建议栈**：`@remotion/sfx`（底） + **earshot**（主） + Kenney/Freesound CC0（补洞）；走宣传片可评估 shotcraft 的音频工作流，使用前确认具体音频许可。

整个视频流水线并非无条件免费：[Remotion 当前许可](https://www.remotion.dev/docs/license/pricing)对个人及至多 3 人公司提供免费许可，其他组织按资格适用相应方案；模型和外部服务另看各自条款。


### 合成、检索与试听的边界（视频 10:38–11:47）

作者尝试了代码合成和 CLAP、AST 等音频理解模型辅助评分，但认为本次尝试的音效质感不佳，且耗时、耗 token，因而改为先找合适的成品音效。这是该次实践结果，不推导为“所有代码合成都不行”；earshot 等原有工具仍可用于适合的电子短音、测量和检索辅助。

Agent 没有接入音频理解工具时，主要依据文件名、标签、说明筛选，不能把“找到文件”当成“已经试听”。先让它给出少量候选，再由人听声音与画面是否匹配；最终在整片里检查音量、切点和是否抢旁白。

Freesound 逐条区分：CC0 可按其条款使用；CC BY 需署名；CC BY-NC 不用于商业项目。视频提到剪辑师分享的音效包，但分享行为本身不代表原始音效授权可转移，仍需追溯来源。Pixabay、Mixkit 与 Envato 也各有自己的许可，不混称为同一种“免费商用”。

### 建立个人音效库（视频 11:47–12:11）

先收听、筛选一小批常用音效，交给 Agent 整理标签；以后优先从本地库取用，缺口再外找或合成。下面是可落地的索引示例，不代表已下载这些文件：

| 类别 | 文件命名示例 | 用途与标注 |
|---|---|---|
| whoosh / swoosh | `whoosh-soft.wav` | 卡片切换；标记轻重、时长、峰值位置 |
| pop / ding / notify | `pop-bubble.wav` | 元素出现、提示、成功反馈；避免每句都响 |
| click / typing | `click-ui.wav`、`typing-loop.wav` | 操作演示；区分单次与循环 |
| paper / camera | `paper-turn.wav` | 翻页、拍照等有实际语义的动作 |
| riser | `riser-short.wav` | 章节开场或情绪过渡，控制频率与音量 |

索引建议记录：相对路径、听感描述、适用动作、时长、来源链接、作者、许可及署名文本；能复用的音效与动效模板一起积累。

<a id="voice"></a>

## 3. 语音工作室、配音与 SRT

专有名词解释：

- SRT：SubRip Subtitle（或SubRip文本），是一种广泛应用于视频字幕的标准文件格式。
- ASR：Automatic Speech Recognition（语音识别），把说话转成文字
- TTS：Text-to-Speech（语音合成），把文字念成语音

### 真人录音与合成配音（视频 04:51–05:29）

作者这期案例的旁白是**本人录制**，并非 TTS；画面展示了降噪、均衡、压缩等后期处理。不想录音时，可让 Agent 接入 TTS 工具替代。录音是否自然、音色是否好听，不宜只归功于某个语音模型。

视频新增的三个独立 TTS 项目如下，与后面的 VoiceStudio / AudioSmith 工作台分层看待；不假定工作台一定集成了相同版本。

| 项目 | 适用能力 | 使用与核实边界 |
|---|---|---|
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 参考音频克隆、少量数据微调 TTS | 上游提供 WebUI；环境、权重和数据要求按所用版本确认 |
| [VoxCPM2](https://github.com/OpenBMB/VoxCPM) | 参考音频克隆与文字描述音色设计 | 适合试配旁白音色；先用术语和中英混读句测样音 |
| [IndexTTS-2.5](https://github.com/index-tts/index-tts) | 参考音频克隆及情绪、语速、发音控制 | 版本见[发布页](https://github.com/index-tts/index-tts/releases)；控制能力与参数按该版本说明核对 |

三者是工具候选，不按视频中的星标数排序。视频称其可免费使用，但部署算力、模型权重、参考音频和生成输出的许可仍要分别确认；声音克隆使用本人或已获授权的参考录音。

### 语音工作台

开源工具：

- VoiceStudio：[VoiceStudio](https://github.com/debpalash/VoiceStudio)，跨平台本地语音创作工具：克隆 / 设计 / 配音 / 听写 / 转写 / 有声书，支持多引擎与多语言，具体功能取决于系统、硬件和引擎
- AudioSmith：[AudioSmith](https://github.com/hehehai/AudioSmith)，Apple Silicon Mac 专用 语音创作台：旁白、故事、有声书、配音、转写、听写，采用 Swift MLX 语音引擎，提供旁白与成片相关工作流


| 维度 | VoiceStudio | AudioSmith | 同 / 异 |
|---|---|---|---|
| **项目目标** | 替代云端 TTS 平台；本机 + Docker + 可选手机预览 | 在 Mac 上把「稿→声→书/片」做完，离线可用 | **同**：本地替代付费云；**异**：前者偏平台，后者偏 Mac 成片工具 |
| **平台** | macOS / Windows / Linux / Docker；Android·iOS 预览；Intel Mac 受限 | **仅** macOS 15+、**M1+** | **异**：覆盖面 vs 深度 |
| **技术栈** | Electron + 多引擎（Python / GGUF / MLX-Audio 等） | Go(MyGo) UI + **Swift MLX** 引擎，**不要 Python** | **异**：引擎枢纽 vs 原生 MLX 一体机 |
| **模型策略** | 提供多种 TTS / ASR；默认引擎与可用模型按安装版本确认 | 按「用途」打包：Qwen3-TTS / Kokoro / Chatterbox / OmniVoice 等；对话专用模型 | **同**：可换模型；**异**：前者引擎超市，后者场景化套餐 |
| **语言覆盖** | 上游标称约 **646** 语种（2026-11-02；随引擎，不代表各语种质量相同） | 中英一等公民；多语靠 OmniVoice / Whisper 等 | **异**：广谱 vs 中英打磨 |
| **核心能力** | 克隆、设计、视频配音、听写、转写、旁白/批量、Local API、MCP、配方与监视文件夹 | 同上 + **Stories（角色/AI 导演/整段对话）**、**Audiobook（章节 M4B）**、**Dub 四步流水线**、Workflows 画布、OpenAI 兼容 API + MCP（工具数量随版本变化） | **同**：语音全链路；**异**：AudioSmith 提供按故事、章节和视频配音组织的界面 |
| **配音深度** | 多说话人配音、导出指南完善 | 人声分离→带说话人转写→翻译→按时长复配；可选整段对话模型 | **同**：本地配音；**异**：AudioSmith 步骤更「成片向」 |
| **Agent 接入** | Local API + MCP + Agent skill | `127.0.0.1:3901` OpenAI 兼容 + 自有 API + MCP | **同**：可给 Cursor/Codex 调 |
| **隐私 / 费用** | 应用本地运行、可免费使用；可选服务及模型许可分别核对 | 本地免费；官网 DMG 需免费账号，或源码自建 | **同**：可本地使用；**异**：分发入口；不代表所有模型均可商用 |
| **版本与验证** | 覆盖多个平台；稳定性需按版本、硬件和引擎实测 | 核对时上游仍说明为 beta；具体版本看发布记录 | **异** |
| **互通** | 自有 `.ovsvoice` 等 | **可导入 VoiceStudio 的 `.ovsvoice`** | AudioSmith 兼容对方音色格式 |

应用许可、模型权重、音色与输出授权应分开确认。[VoiceStudio 许可说明](https://github.com/debpalash/VoiceStudio#license--responsible-use)明确提示这些许可相互独立；[AudioSmith 模型表](https://github.com/hehehai/AudioSmith#models)将 OmniVoice 列为 **CC BY-NC 4.0（非商业）**。因此不能仅凭“本地免费”将其作为商业视频默认配音模型。

应用场景怎么选（选型建议，未逐项实测）：

| 你的场景 | 更贴谁 | 原因 |
|---|---|---|
| Windows / Linux / 服务器 Docker | **VoiceStudio** | 跨平台 + 多引擎 + Docker |
| 只要 Apple Silicon Mac、要故事/有声书/配音成片体验 | **AudioSmith** | 提供 Stories / M4B / Dub / Workflows |
| 需要多语种覆盖与引擎试验 | **VoiceStudio** | 按所需语种和引擎先测样音；标称覆盖不保证效果 |
| 中英内容、对话戏、章节有声书、给 Agent 打成 OpenAI TTS | **AudioSmith** | 对话模型 + ACX/M4B + `/v1/audio/speech` |
| Remotion / 讲解片旁白 TTS（本机出 wav/m4a） | **两者都行** | 都有本地 TTS + API；按硬件、模型许可、样音和工作流实测选择 |
| 不想碰 Python、只要 MLX | **AudioSmith** | 明确无 Python |
| 需要手机端预览 / 多种加速后端 | **VoiceStudio** | 有移动端预览与多加速后端 |


### SRT 是配音与画面的时间依据（视频 05:29–06:56）

逐字稿定义“说什么”，最终录音定义“何时说”；SRT 记录每条字幕的序号、起止时间及文本。画面和动效可引用这些时间，避免按文字长度猜语速。只有稿件、没有音轨时，生成的时间只能是估计。

1. 先完成录音或 TTS，提供与该音轨匹配的脚本供校对。
2. 用 ASR / 对齐工具取得时间戳。作者使用社区实现 [whisper.cpp](https://github.com/ggml-org/whisper.cpp) 运行 Whisper `large-v3-turbo`；也提到飞书妙记、剪映等转写工具。普通聊天文本能力不等于已接入语音识别，需检查当前 Agent 的实际工具。
3. 对照原稿修正人名、专业术语、英文品牌、同音字；原稿只辅助校对，不把实际未念出的内容硬塞进字幕。
4. 按语义和停顿断句。视频建议多数字幕约 **8～18 个汉字**宽，避免长句挤成两行；这是示例约束，最终以画幅、字号和可读性检查为准。
5. 输出 SRT 并抽查开头、中段、结尾与长停顿，确认没有重叠、漏句或持续偏移；脚本辅助校对仍不能保证零错误。
6. 在 Remotion 中解析并编排字幕；[官方 `parseSrt()`](https://www.remotion.dev/docs/captions/parse-srt)负责解析文件，不会替代 ASR 或验证音画是否真实同步。普通句级 SRT 也不自动具备逐字高亮所需的字级时间戳。

**留白与改稿的联动**：章节切换或动画展示时间不够时，可在句间或章间调整停顿；同步修改音频、受影响字幕、后续场景与音效时间。不能只延长画面而继续沿用旧 SRT。不同 ASR 模型的速度、内存、质量取舍先在本机短音频上试，不把视频里的内存估算当成所有设备的硬门槛。

可复用的任务描述（据视频整理）：

> 依据旁白音轨生成 SRT，参考脚本校对术语与错字；按语义和停顿断句，多数字幕控制在约 8～18 个汉字的宽度。需要为章节或动画增加停顿时，同步更新音频、SRT 和后续场景时间；最后检查字幕与实际配音同步。

<a id="styles"></a>

## 4. 风格

- [sy-style-100](https://github.com/xiaoxiong20xx-code/sy-style-100)
- [lemo-opuscar在线画廊](https://github.com/lemomo-ai/lemo-opuscar)：视频展示了剪辑纪实、手绘、立体书、3D 等方向，适合先看样片再研究对应方法。
- [huashu-art-motion艺术动画](https://github.com/alchaincyf/huashu-art-motion)：艺术画风与讲解语法可分开选择，如像素、绘画、白板、数学动画与动态文字。
- [vox-director依托Atlas API，可能收费](https://github.com/Alisa0808/vox-director)：偏 Vox 式讲解与拼贴叙事；其自动化链路和外部服务依赖应先核对，不能等同于全本地免费。
- [srt-whiteboard手绘](https://github.com/geeklee/srt-whiteboard-animation)：手绘/白板讲解候选，重点检查绘制节奏能否贴合旁白。
- [sweety-handdraw手绘](https://github.com/threerocks/sweety-handdraw-video)：手绘表现候选，先看线条、揭示方式和文字可读性。
- [stickman火柴人](https://github.com/kaomei/stickman-video-director)：视频展示黑白、彩色、壁画等不同方向，适合用角色动作解释观点。
- [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)：新增风格参考，涵盖插画、2.5D/3D、图形、动态排版与拼贴等。**上游核实**：这是附提示词和源码的 15 支短片项目，不能仅凭视频里的 `skill add` 示意就当作现成可安装 Skill；按 README 研究与复用。


视频 08:14–10:38 的选型补充：作者明确未逐个实测这些社区资源。先选符合题材的画风和讲述方式，再检查底层是否使用 Remotion、依赖是否可运行、产物能否接入自己的工程；代码动画项目之间有共同技术，但并非直接兼容。样片数量和风格数量只是该视频录制时的展示，不作为固定规格。

无参考时可先做短样片明确偏好；有参考时，指定要学的段落、配色、构图和运动逻辑，避免一句“照着做”让 Agent 漫无目的地抽帧猜测。

<a id="templates"></a>

## 5. 视频模板

固定的内容编排可用于系列视频复用；标题、字幕、片尾等组件也可单独沿用。复用价值取决于素材、参数、节奏是否可替换，应按实际发布需求试用。

- [motiontemplates](https://github.com/motiontemplates/all)


### 模板不是整包照搬（视频 09:16–10:38）

- `motiontemplates` 在视频中用于真人出镜/口播讲解版式参考，包含横竖屏方向；`video-shotcraft` 更偏产品宣传片镜头工具箱，不能仅按“都有模板”视为同一用途。
- 一个包跑起来太重、效果不合适或千篇一律时，可以只复用合适的布局、转场、动画组件与已验证音效，而非同时启用整包流程。
- 阅读 `SKILL.md` 的流程、避坑和经验，以及 `templates/`、`scripts/`、`references/`、`sfx/` 等实际目录，挑出能接入自己项目的部分；目录是否存在以具体仓库为准。
- 复用时保留适用许可和来源，并把自己验证过的组件、输入参数与使用场景整理成个人动效库。镜头数不是 SFX 数，原清单中 shotcraft 的音效数量仍不据样片数推断。

<a id="icons"></a>

## 6. 表情、品牌、图标与可复用角色素材

以下为选型摘要，未逐素材审计授权；下载时记录具体版本与条款，品牌商标规则与素材版权许可分别确认。

| 类别 | 名称 | 链接 | 适合 | 授权备注 | 默认选型 |
| --- | --- | --- | --- | --- | --- |
| AI / 品牌 logo | Lobe Icons | https://github.com/lobehub/lobe-icons | ChatGPT、Claude、DeepSeek 等 AI 品牌 SVG/PNG/WebP | 开源可用；商标商用仍受品牌方约束 | ✅ 品牌首选 |
| AI / 品牌 logo | Simple Icons | https://simpleicons.org/ | 通用科技品牌单色 SVG | CC0；商标规则另看 | Lobe 没有时备用 |
| AI / 品牌 logo | Brandfetch | https://brandfetch.com/ | 按域名拉官方品牌资源 | 看其 API/使用条款 | 需要官方高清时 |
| 通用 UI 图标 | Lucide | https://lucide.dev/ | 文件夹、回形针、箭头、靶子等线框图标 | MIT | ✅ UI 小件首选 |
| 通用 UI 图标 | Tabler Icons | https://github.com/tabler/tabler-icons | 同类 UI 图标；数量随版本更新 | MIT | ✅ Lucide 缺图时 |
| 通用 UI 图标 | Phosphor Icons | https://phosphoricons.com/ | 多线宽/填充风格 UI 图标 | MIT | 需要粗细/填充变体时 |
| 通用 UI 图标 | Heroicons | https://heroicons.com/ | Tailwind 风格 outline/solid | MIT | 可选 |
| 聚合搜索 | Iconify | https://iconify.design/ | 一站搜 Lucide/Tabler 等多数图标集 | 各子库授权不同 | ✅ 统一搜入口 |
| 小动物 / 插画 | Neu Icons | https://github.com/neuicons/neu | 含 Animal 等分类 SVG | 按其仓库许可 | 矢量小动物首选候选 |
| 小动物 / 表情 | Twemoji | https://github.com/twitter/twemoji | 开源 emoji 图（含动物） | CC-BY 4.0（需署名） | 表情/动物备选（记得署名） |
| 场景插画 | unDraw | https://undraw.co/ | 可改色场景插画 | 看站点条款（一般可商用） | 大场景插画首选候选 |
| 场景插画 | Storyset | https://storyset.com/ | 可编辑场景插画 | 免费档常需署名 | 慎用（署名） |
| 动效素材 | LottieFiles | https://lottiefiles.com/ | 小动画点缀（Lottie JSON） | 单条素材授权各异 | ✅ 动效首选 |

默认选型（一句话）

- **品牌 logo** → Lobe Icons（没有再用 Simple Icons / Brandfetch）
- **UI 小件**（文件夹、回形针、箭头、靶子等）→ Lucide，缺图用 Tabler
- **统一搜索** → Iconify
- **动效点缀** → LottieFiles
- **小动物 / 大插画** → Neu Icons / Twemoji / unDraw（按是否需要署名选型）

### 角色小动画与透明底素材（视频 03:40–04:48）

作者把平时积累的小玩偶图片、短动画反复用于不同视频；它们是独立制作的素材，不是每次都由 Remotion 从零绘制。视频中的制作方式是：

1. 用图像生成工具先做统一角色的绿幕图片，再以该图驱动视频模型生成动作。
2. 对绿幕短片做色度抠像，调节强度并观察主体边缘、阴影是否被误抠除；残余绿边可按素材情况用 HSL 或去溢色处理，避免误伤角色自身的绿色。
3. 导出带 Alpha 的素材。作者示例选择 **HEVC (Alpha)**；使用前验证自己的剪辑器和渲染链支持，普通 MP4/H.264 导出不等于保留透明度。不兼容时可另测支持 Alpha 的格式或 PNG 序列。
4. 将原图、原始短片和透明版本入库，在不同场景复用；提示动作、时长、入场位置，保留同一角色的外形与比例。

视频模型路线更适合试自然的角色动作，代码路线便于精确控制和参数复用；按具体动作选择，不把作者的体验泛化成模型始终优于代码。平台赠送积分只作为当时制作素材的成本背景，不当作长期额度承诺。裁切和蒙版应针对有权编辑的素材，并遵守来源署名和使用条件。

整理建议：为角色素材补上动作、朝向、时长、是否循环、尺寸、透明格式与许可说明，方便 Agent 正确选择。

## 7. 官方 Skills 与制作环节补充

<a id="production"></a>

核对日期：2026-11-02。以下为外部资源整理，未执行安装；工具、素材库、Skill 和 MCP 分别标注，不将所有条目统称为已安装的 Skills。

| 环节 | 资源 / 身份 | 产物与使用方式 |
|---|---|---|
| Remotion 官方 Skills | [官方文档](https://www.remotion.dev/docs/ai/skills) · [remotion-dev/skills](https://github.com/remotion-dev/skills) | 覆盖创建、预览、渲染、字幕、动效等；可按官方说明使用 `npx skills add remotion-dev/skills`。这是 Skill 指导，成片仍由 Remotion 项目渲染 |
| 社区导演与风格 | 上文 Remotion 部分的 shotcraft / talkcraft / motion-design-skill，以及风格资源链接 | 均按社区资源看待，先读各项目 README、依赖和样片，再选与本片目标相符的一套 |
| 真实录屏 | [OBS Studio](https://obsproject.com/)，工具官方 | 录制产品操作、游戏实机、摄像头和音频；录制素材交给 Remotion 编排。OBS 本身不是 Skill |
| 补充镜头 / 图片 | [Pexels](https://www.pexels.com/)，素材站；[许可说明](https://www.pexels.com/license/) | 用于 B-roll、背景和封面；属于站点许可，不标成 CC0 |
| BGM / SFX / 镜头 | [Mixkit](https://mixkit.co/)，素材站；[分类许可](https://mixkit.co/license/) | 补充原清单较少覆盖的背景音乐与镜头；按具体条目选择 Free / Restricted 等许可，不能全站视为同一许可 |
| 本地字幕转写 | [whisper.cpp](https://github.com/ggml-org/whisper.cpp)，工具项目 | 已有录音转写为字幕文件，核对人名、术语与时间轴后再排字幕；它是社区实现，不是语音模型厂商官方 Skill |
| 字幕版式 | Remotion 官方 Skills 中的 `remotion-captions` 与[字幕文档](https://www.remotion.dev/docs/captions/) | 将文字和时间戳做成视频字幕；区分 ASR 转写和字幕绘制 |
| 中文字体 | [Noto CJK](https://github.com/notofonts/noto-cjk)，字体项目 | 字幕、标题和封面保持统一字形；随素材记录字体许可，渲染前确认字体加载完成 |
| 转码 / 音频处理 | [FFmpeg 文档](https://ffmpeg.org/documentation.html)，工具官方入口 | 裁切、转码、提取音轨与响度处理；属于 CLI 工具，不假定已存在官方 Skill/MCP。本轮文档抓取超时，未核对具体命令 |
| 技术概念 / 系统结构图 | [Anatomy](https://github.com/wheresryan22/anatomy)，社区 Skill | 视频 09:43 左右展示，用交互式等轴测结构图解释机器或复杂系统；上游主要产出 SVG/HTML 等，不是完整视频流水线。作为讲解素材接入或录制时另处理时间轴与导出 |
| 像素素材与片头 | [Game 像素 VFX](Game.md#pixel-vfx)与[仓库内 Skill](VFX/scenario-pixel-vfx/SKILL.md) | PNG 帧 / GIF 用于游戏展示、像素转场、视觉点缀；保持整数倍缩放 |

### 截图、录屏与素材收集（视频 03:00–03:40）

本地文件和可访问网页可由 Agent 协助查找、分类、匹配脚本；其他应用中的素材需要相应操作能力，可能依赖 MCP 或 Computer Use。技术上能访问不代表收集结果符合讲解需求，最后仍要人工检查截取范围、内容和清晰度。

基础查找、重命名、归类可先用成本较低的模型尝试；复杂画面判断再升级工具或模型。给 Agent 一个“可用素材清单”比只给一堆文件更可靠：建议列相对路径、来源、说明、录屏可用起止段、对应脚本段落及待补缺口，不让它用无关画面填空。

### 配音与音效的交接

旁白先导出 WAV/M4A，确定读音、停顿和实际时长，再锁定镜头与字幕时间轴。耳听检查仍是最终验收；earshot 的描述与测量可提供辅助证据。

earshot 完整调用例子为 `earshot sfx render whoosh_fast/crisp -o whoosh.wav`，见[上游 README](https://github.com/Leonxlnx/earshot)。SFX 短音与持续 BGM 分轨处理，旁白出现时调整音乐音量。

## 8. 个人发布工作流

<a id="workflow"></a>

1. 明确主题、受众、目标时长与画幅，写旁白稿和镜头提纲。
2. 收集本人录屏、截图、B-roll、图标、字体；同时记录素材来源与许可。
3. 录制或合成旁白，校对术语与读音；以最终音轨建立字幕时间轴。
4. 用 Remotion 官方 Skills 打底，按宣传片或口播讲解需要选社区 Skill；沿用合适模板的标题、字幕和片尾组件。
5. 加 SFX/BGM，检查旁白清晰度、切点、峰值与尾音；预览关键帧并完整播放成片。
6. 按目标平台当次要求导出，检查横竖版裁切、字幕安全区、封面与简介；保留可编辑工程、音轨和字幕。

### 脚本的三层内容（视频 01:02–03:00）

| 层次 | 要准备什么 | 交给 Agent 时的约定 |
|---|---|---|
| 逐字旁白 | 实际要念出的每一句话 | 个人经验由本人提供事实与体感，AI 可辅助校验、精简和组织；不是让模型虚构自己的经历 |
| 屏幕展示 | 旁白不念但必须出现的提示词、示例、操作说明 | 明确标注“仅屏幕展示”“必须完整保留”，避免被压缩成几个要点 |
| 可用素材与必要动作 | 每个段落可用的截图、录屏、角色动作 | 收集后先由 Agent 建议匹配，人再确认；重要互动单独注明，不必提前写死每个镜头 |

作者不逐段编排整片动画，但不是完全不约束：必讲操作、关键示例、环境要求等要清楚记录，长期规则可写入项目 `AGENTS.md`。这属于视频制作项目的经验建议，不是本仓库新增的执行规则。

### 分阶段交付与返工控制（视频 06:56–08:14）

1. **开工前**：脚本、素材、配音与 SRT 齐备，列明必讲内容和缺口；检查运行环境、依赖与字体。不能把脚本中的环境配置“讲解内容”误当作已经执行了环境检查。
2. **先试样**：约 1～2 分钟测试真实素材、旁白、字幕和转场；风格不明确时先看到初版，再给具体修改点。
3. **定标准后扩展**：按短片中确定的背景、字体、动画密度和信息层级制作长片；短片通过不代表其余章节免验收。
4. **修改时联动**：换旁白、插停顿、延长演示都会影响后续时间，更新音频、SRT、场景和音效后再预览。
5. **验收与沉淀**：检查必讲内容是否遗漏、素材有无错配、字幕与声音是否同步，再把合用的镜头和音效放入自己的库。视频中一小时或 token 消耗只是作者案例，不作为本项目成本估算。

本节是在原有发布流程上的制作细化；平台上传、封面和发布要求仍按上面的流程执行，视频未展开的平台运营内容不冒充作者观点。

这是制作建议，未代为上传、发布或接入任何平台账号。品牌图标、音色与素材授权按实际条目确认；“个人发布”也可能含商业用途，不能只凭是否收费判断模型许可。

## 待核实范围

未逐项安装实测语音工具与风格 Skills。VoiceStudio / AudioSmith 的细分功能、平台兼容、模型效果与 API 以所用版本为准；不以星标或平台数量推断稳定性。shotcraft 的音频数量、SoundCN 及图标/插画等具体素材的许可未逐文件审计；暂不纳入的云音效服务也未逐项核价。所有资源入口继续保留供后续核实。

本次视频核对范围：引言 00:12–01:02、脚本 01:02–03:00、素材 03:00–04:51、配音与 SRT 04:51–06:56、制作方法 06:56–08:14、资源推荐与复用 08:14–10:38、音效 10:38–12:15 均已覆盖。正文记录了制作方法、缺失资源及适用边界；字幕断句示例、素材索引和验收步骤为据视频整理的落地方式，未实际安装或测试视频推荐的全部工具。
