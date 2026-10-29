## Skills列表

### 1. 完全免费文生特效方案（无订阅 / 无日限额度）

专注像素vfx特效生成和导出

#### A 线：精灵表 / PNG（跨引擎素材，推荐你优先）

| 方案 | 文生方式 | 最终产物 | Godot | Unity | 授权 / 费用 | 和你目标的匹配 | 备注 |
|---|---|---|---|---|---|---|---|
| **[Pixelbolt](https://skulitom.github.io/Pixelbolt/)** ★推荐默认 | Agent/CLI 写 JSON 配方 → **本地渲染**（无云生图） | 透明 PNG 精灵表、atlas、GIF、编号帧 | 导入 SpriteFrames / 精灵表 | Sprite Editor 切片 / 动画 | **MIT**，本地免费 | **最贴**：像 Unity 习惯的精灵素材；可脚本化 | Star 少不影响可用性；可复现、无额度 |
| **[Scenario Pixel VFX Forge](https://www.scenario.com/explorations/pixel-vfx-forge/)** + 开源 Claude skill | 自然语言 → 分层配方 → **浏览器/本地免费渲染** | 精灵表、单帧、GIF、JSON atlas、**Godot 4 SpriteFrames** | 可直接用导出包 | 用表自行切片即可 | 探索页免费；skill 开源 | 很贴；上手快、社区热 | X 上「一句话火球→Godot」多指这条；偏像素战斗/法术 |
| 本机 **scenario-pixel-vfx** 类路径 | 文字 → 效果配方 → 出帧 | 精灵表 / GIF / 帧 | 同左 | 同左 | 本地确定性，无云额度 | 与上同源思路 | 适合已接入 Agent 流水线时 |

#### B 线：引擎内程序化（不是精灵素材包）

| 方案 | 文生方式 | 最终产物 | Godot | Unity | 授权 / 费用 | 和你目标的匹配 | 备注 |
|---|---|---|---|---|---|---|---|
| **[combat-vfx-demo](https://github.com/yuewen-huang/combat-vfx-demo)** | Agent Skill：白话连招 → 写时间轴 | **`.tscn` + `combo.json` / `style.json` + 运行时 `_draw`/着色器**；审片可出 GIF/帧表 | **原生**：场景里直接播刀光/魔法/hit-stop | **基本不直接适用**（不是 PNG 管线） | **PolyForm Noncommercial**：个人/学习免费；**商用须另授权** | 仅当你已定 Godot + 连招手感、不急需跨引擎素材 | ≈33★；无外部美术；**不是** Godot 特效的唯一标准做法 |
| 同类 Godot procedural / VFX Skill（如 vfx-generator、scenario-godot-vfx 等） | Agent 写粒子/几何特效场景 | `.tscn` / `.gd` 等 | 引擎内用 | 一般不跨 | 视各仓库 License | 同属 B 线补洞，非精灵表 | 检索时别和 A 线混搜 |


#### A vs B 怎么理解（对照 Unity）

| | A 精灵表 / PNG | B `.tscn` + JSON + 运行时绘制 |
|---|---|---|
| 像 Unity 什么 | Sprite + Animation / 粒子贴图序列 | 代码画 Trail、程序化 Mesh、自写 combo 数据 |
| 磁盘上有没有特效图 | **有**，可当素材复用 | **往往没有**；画面现场画 |
| 跨引擎 | 容易（Godot + Unity） | 绑在 Godot 运行时 |
| Godot 项目里常见吗 | **2D 很常见** | 也有（粒子/着色器/程序化），但不是唯一标准 |
| 你更熟的路径 | **是** | 否 |

#### 选型结论

| 你的情况 | 选 |
|---|---|
| 要当游戏素材、流程像 Unity、Godot/Unity 都能用 | **A：Pixelbolt（默认）**；要浏览器快试再加 Pixel VFX Forge |
| 只要 Godot、要整段连招 + 打击感、接受非商用协议 | 再看 **B：combat-vfx-demo** |
| Star 多少 | **不当筛选条件**；用产物形态 + 授权 + 是否进引擎来判 |

**一句话推荐**：免费前提下优先 **Pixelbolt（A 线精灵表）**；Scenario Pixel VFX Forge 作同路备选；**combat-vfx-demo 不进默认推荐**，除非明确走 Godot 程序化连招。

### 2. Remotion 做视频和动态图形

用 React 创建视频和动态图形，偏向于产品宣传，口播讲解，技术讲解等视频

底座装 remotion-dev/skills；宣传片加 video-shotcraft；口播讲解加 video-talkcraft；想更像动效导演再叠 motion-design-skill。这四套是目前 X 上既有安装量、又有真实成片帖、且真正落在 Remotion 上的最优组合。

- 官方地址：[Remotion Skills](https://www.remotion.dev/docs/ai/skills)
- 社区产品宣传片首选：[video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) 
- 社区口播讲解片首选：[video-talkcraft](https://github.com/Vincentwei1021/video-talkcraft)
- 社区审美层：[LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)


### 3. SFX 音效(Sound Effects)

代码合成，可以用作补全Remotion/sfx自带音效不够的情况


| 方案 | 费用 | 规模/特点 | 怎么进 Remotion | 适合 |
|---|---|---|---|---|
| [@remotion/sfx](https://www.remotion.dev/docs/sfx/) | 免费 | 少量 whoosh/whip 等 | `import` 直接用 | 起步转场 |
| [earshot](https://github.com/Leonxlnx/earshot) | 开源免费 | ~252 个代码合成音效；可 `kit`/`describe` | `sfx render` → WAV → `<Audio>` / `staticFile` | 主补库、切点对齐、Agent 听感 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) 自带包 | 开源免费 | ~149 SFX + BGM | Skill/流水线内嵌，或拷到 `public/sfx` | 产品宣传片一站式 |
| [Kenney](https://kenney.nl/assets?q=audio) | CC0 免费 | 游戏/UI 音效包，量大 | 下 WAV → `public/sfx` | 点击、UI、通用短音 |
| [Freesound](https://freesound.org)（选 CC0） | 免费（需选许可证） | 海量真人录音 | 下 WAV → `public/sfx` | 真实质感、冷门声 |
| [SoundCN](https://github.com/kapishdima/soundcn) / [soundcn.xyz](https://soundcn.xyz) | 开源/免费素材 | UI 点击类 | 导出文件再挂 `<Audio>` | 网页式交互音 |

**已排除**：ElevenLabs、SFXMint、Lots of Sounds（API/额度/商用门槛）、任何按月配额的文生音效。

**推荐默认栈（全免费）**：`@remotion/sfx`（底） + **earshot**（主） + Kenney/Freesound CC0（补洞）；走宣传片就优先用 shotcraft 自带那包。

### 4. 语音工作室

专有名词解释：
- ASR： Automatic Speech Recognition（语音识别），把说话转成文字
- TTS： Text-to-Speech（语音合成），把文字念成语音

开源工具：
- VoiceStudio：[VoiceStudio](https://github.com/debpalash/VoiceStudio)，全平台本地版 ElevenLabs：克隆 / 设计 / 配音 / 听写 / 转写 / 有声书，「引擎多、语言广、到处能跑」
- AudioSmith：[AudioSmith](https://github.com/hehehai/AudioSmith)，Apple Silicon Mac 专用 语音创作台：旁白、故事、有声书、配音、转写、听写，「无 Python、全 MLX、成片工作流打磨深」


| 维度 | VoiceStudio | AudioSmith | 同 / 异 |
|---|---|---|---|
| **项目目标** | 替代云端 TTS 平台；本机 + Docker + 可选手机预览 | 在 Mac 上把「稿→声→书/片」做完，离线可用 | **同**：本地替代付费云；**异**：前者偏平台，后者偏 Mac 成片工具 |
| **平台** | macOS / Windows / Linux / Docker；Android·iOS 预览；Intel Mac 受限 | **仅** macOS 15+、**M1+** | **异**：覆盖面 vs 深度 |
| **技术栈** | Electron + 多引擎（Python / GGUF / MLX-Audio 等） | Go(MyGo) UI + **Swift MLX** 引擎，**不要 Python** | **异**：引擎枢纽 vs 原生 MLX 一体机 |
| **模型策略** | 默认 OmniVoice；可换十几套 TTS + 多套 ASR | 按「用途」打包：Qwen3-TTS / Kokoro / Chatterbox / OmniVoice 等；对话专用模型 | **同**：可换模型；**异**：前者引擎超市，后者场景化套餐 |
| **语言覆盖** | 标称约 **646** 语种（随引擎） | 中英一等公民；多语靠 OmniVoice / Whisper 等 | **异**：广谱 vs 中英打磨 |
| **核心能力** | 克隆、设计、视频配音、听写、转写、旁白/批量、Local API、MCP、配方与监视文件夹 | 同上 + **Stories（角色/AI 导演/整段对话）**、**Audiobook（章节 M4B）**、**Dub 四步流水线**、Workflows 画布、OpenAI 兼容 API + MCP（约 33 tools） | **同**：语音全链路；**异**：AudioSmith 成片工作流更产品化 |
| **配音深度** | 多说话人配音、导出指南完善 | 人声分离→带说话人转写→翻译→按时长复配；可选整段对话模型 | **同**：本地配音；**异**：AudioSmith 步骤更「成片向」 |
| **Agent 接入** | Local API + MCP + Agent skill | `127.0.0.1:3901` OpenAI 兼容 + 自有 API + MCP | **同**：可给 Cursor/Codex 调 |
| **隐私 / 费用** | 本地免费；无付费云；赞助可选 | 本地免费；官网 DMG 需免费账号，或源码自建 | **同**：核心零订阅；**异**：分发入口 |
| **成熟度** | 星标与下载量很大，跨平台稳定版更「主流」 | `0.4.0-beta`，Mac 体验细，生态尚小 | **异** |
| **互通** | 自有 `.ovsvoice` 等 | **可导入 VoiceStudio 的 `.ovsvoice`** | AudioSmith 兼容对方音色格式 |

 应用场景怎么选

| 你的场景 | 更贴谁 | 原因 |
|---|---|---|
| Windows / Linux / 服务器 Docker、要一套「到处能跑」 | **VoiceStudio** | 跨平台 + 多引擎 + Docker |
| 只要 Apple Silicon Mac、要故事/有声书/配音成片体验 | **AudioSmith** | Stories / M4B / Dub / Workflows 更深 |
| 极多语种、引擎试验、和 ElevenLabs「能力对标」叙事 | **VoiceStudio** | 语言与引擎目录更广 |
| 中英内容、对话戏、章节有声书、给 Agent 打成 OpenAI TTS | **AudioSmith** | 对话模型 + ACX/M4B + `/v1/audio/speech` |
| Remotion / 讲解片旁白 TTS（本机出 wav/m4a） | **两者都行** | 都有本地 TTS + API；Mac 上 AudioSmith 更「开箱」，跨机 VoiceStudio 更稳 |
| 不想碰 Python、只要 MLX | **AudioSmith** | 明确无 Python |
| 要手机端预览 / 极广硬件 | **VoiceStudio** | 有移动端预览与多加速后端 |
