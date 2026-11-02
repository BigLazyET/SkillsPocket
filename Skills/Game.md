# Game：游戏开发资源与 Skills

[项目首页](../README.md) · [Video 清单](Video.md)

聚焦游戏素材、引擎工作流、官方 MCP/Skills 与社区接入。外部链接不代表已安装；仓库的 MIT 许可不替代外部工具、模型和素材自身的许可。核对日期：2026-11-02；未经实测的体验判断不作为能力保证。

## 导航

- [像素角色 / 武器 / 特效](#pixel-vfx)
- [像素图块 / 道具](#tiles)
- [Godot 接管范围与人工验收](#godot-workflow)
- [引擎、官方 MCP/Skills 与社区接入](#engines)
- [本仓库可用资源与跨用途素材](#local-assets)

<a id="pixel-vfx"></a>

## 1. 像素角色/武器/特效生成

以像素 VFX 生成和导出为主。Pixelbolt 也覆盖精灵、图块与图标；本仓库的 scenario-pixel-vfx 渲染脚本专注特效，不负责生成角色或武器底图，不能视为完整的角色逐帧动画方案。

### A 线：精灵表 / PNG（跨引擎素材，推荐你优先）

| 方案 | 文生方式 | 最终产物 | Godot | Unity | 授权 / 费用 | 和你目标的匹配 | 备注 |
|---|---|---|---|---|---|---|---|
| **[Pixelbolt](https://skulitom.github.io/Pixelbolt/)** ★推荐默认 | Agent/CLI 写 JSON 配方 → **本地渲染**（无云生图） | 透明 PNG 精灵表、atlas、GIF、编号帧 | 导入 SpriteFrames / 精灵表 | Sprite Editor 切片 / 动画 | **MIT**，本地免费 | **最贴**：像 Unity 习惯的精灵素材；可脚本化 | 本地配方渲染可复现，无云端生成额度 |
| **[Scenario Pixel VFX Forge](https://www.scenario.com/explorations/pixel-vfx-forge/)** + 可下载 Agent Skill | 自然语言 → 分层配方 → **浏览器/本地免费渲染** | 精灵表、单帧、GIF、JSON atlas、**Godot 4 SpriteFrames** | 可直接用导出包 | 用表自行切片即可 | 探索页可使用；Skill 的再分发许可按上游分发物核对 | 适合浏览器试配方和导出 | 偏像素战斗/法术；网页导出与本地脚本能力分开判断 |
| 本仓库 **[scenario-pixel-vfx](VFX/scenario-pixel-vfx/SKILL.md)** | 文字 → 效果配方 → 本地出帧 | PNG 精灵表、JSON atlas、GIF、可选单帧 | 需切片或转换为 SpriteFrames，脚本不直接导出该资源 | Sprite Editor 切片 / 动画 | 本地渲染无云额度；云端生成角色另计费用，许可分别核对 | 适合 Agent 本地素材流水线 | 支持带背景预览；与网页 Forge 的导出范围不同 |
| **[Pixelfx](https://github.com/patch-gg/pixelfx)** | 上游标称 244 个程序化特效（2026-11-02 核对） + 可自写新特效 | sheet + Aseprite 风格 JSON，再导入 | sheet + Aseprite 风格 JSON，再导入 | sheet + Aseprite 风格 JSON，再导入 | MIT | 同上 | 适合已接入 Agent 流水线时 |

### B 线：引擎内程序化（不是精灵素材包）

| 方案 | 文生方式 | 最终产物 | Godot | Unity | 授权 / 费用 | 和你目标的匹配 | 备注 |
|---|---|---|---|---|---|---|---|
| **[combat-vfx-demo](https://github.com/yuewen-huang/combat-vfx-demo)** | Agent Skill：白话连招 → 写时间轴 | **`.tscn` + `combo.json` / `style.json` + 运行时 `_draw`/着色器**；审片可出 GIF/帧表 | **原生**：场景里直接播刀光/魔法/hit-stop | **基本不直接适用**（不是 PNG 管线） | **PolyForm Noncommercial**：限许可允许的非商业用途；**商用须另授权** | 仅当你已定 Godot + 连招手感、不急需跨引擎素材 | 程序化绘制，无需预制特效贴图；**不是** Godot 特效的唯一标准做法 |
| 同类 Godot procedural / VFX Skill（检索线索：vfx-generator、scenario-godot-vfx；未确认具体仓库） | Agent 写粒子/几何特效场景 | `.tscn` / `.gd` 等 | 引擎内用 | 一般不跨 | 视各仓库 License | 同属 B 线补洞，非精灵表 | 仅作检索线索；仓库、功能与许可待核实，不作为已验证安装方案 |


### A vs B 怎么理解（对照 Unity）

| | A 精灵表 / PNG | B `.tscn` + JSON + 运行时绘制 |
|---|---|---|
| 像 Unity 什么 | Sprite + Animation / 粒子贴图序列 | 代码画 Trail、程序化 Mesh、自写 combo 数据 |
| 磁盘上有没有特效图 | **有**，可当素材复用 | **往往没有**；画面现场画 |
| 跨引擎 | 容易（Godot + Unity） | 绑在 Godot 运行时 |
| Godot 项目里常见吗 | **2D 很常见** | 也有（粒子/着色器/程序化），但不是唯一标准 |
| 你更熟的路径 | **是** | 否 |

### 选型结论

| 你的情况 | 选 |
|---|---|
| 要当游戏素材、流程像 Unity、Godot/Unity 都能用 | **A：Pixelbolt（默认）**；要浏览器快试再加 Pixel VFX Forge |
| 只要 Godot、要整段连招 + 打击感、接受非商用协议 | 再看 **B：combat-vfx-demo** |
| Star 多少 | **不当筛选条件**；用产物形态 + 授权 + 是否进引擎来判 |

**一句话推荐**：免费前提下优先 **Pixelbolt（A 线精灵表）**；Scenario Pixel VFX Forge 作同路备选；**combat-vfx-demo 不进默认推荐**，除非明确走 Godot 程序化连招。


<a id="tiles"></a>

## 2. 像素图块系统/道具精灵

| 方案 | 管什么 | 费用 / 许可 | 备注 |
|---|---|---|---|
| [Kenney](https://kenney.nl/assets) | 树、建筑、家具、自然物、简易城镇等现成精灵/图块包 | CC0，可商用 | 可按同一素材包保持风格统一；适合前期铺关，后期按需换皮 |
| [Autotiler](https://github.com/itsjavi/autotiler) | 几块地形模板 → 扩成 47 格 blob / 导出 Godot·Tiled | MIT，本地/网页 | 负责拼缝规则，不负责「画好看」；常和 Kenney 或自有地块模板搭配 |


<a id="godot-workflow"></a>

## 3. Godot MCP/Skills

以下是 Agent 辅助开发的任务分工建议，并非任意 MCP 服务的能力清单。Skill 提供指导，MCP 暴露具体操作，Agent 也可直接编辑脚本和场景文本；Visual Studio 是 IDE，不适合与 MCP/Skills 直接比较。表中强弱是工作分工判断，场景编辑、运行、截图及调试须以所接服务的工具列表为准。

| 事项 | 建议辅助程度 | 说明 |
|---|---|---|
| 场景节点树、.tscn 搭骨架 | ✅ 强 | CharacterBody2D、Camera2D、TileMapLayer 等 |
| SpriteFrames / AnimationPlayer 切片建动画 | ✅ 强 | 需清晰命名与帧约定 |
| AnimationTree 状态与 transition 骨架 | ✅ 强 | 可按约定生成条件、连线和 xfade 初值，需运行验证 |
| 脚本驱动参数（velocity、floor、input） | ✅ 强 | 纯代码，最适合 Codex |
| 玩法状态机 / 技能树逻辑 | ✅ 强 | GDScript/C# FSM、技能 CD、连招 |
| 信号连接、输入映射、层与 mask 初值 | ✅ 中强 | 可生成初值，需核对信号签名及碰撞层规范 |
| TileMapLayer 铺关、TileSet terrains 规则套用 | ✅ 中 | 规则可由 AI 配，关卡审美要人 |
| UI / HUD 布局与锚点 | ⚠️ 半 | 能搭，像素对齐常要人挪 |
| 碰撞形状「手感精度」 | ❌ 弱→人 | 可初值，精调靠实机 |
| 攻击判定与动画帧精确对齐 | ❌ 弱→人 | 需打帧或调试绘制 |
| 数值平衡（伤害、CD、击退） | ❌ 设计 | AI 可给表，最终玩出来改 |
| 美术风格统一、光影、粒子审美 | ❌ 人 | 技术接线可 AI |
| 音频同步（脚步踩帧） | ⚠️ 半 | 可挂方法轨，节奏要听 |
| 存档、设置、本地化脚手架 | ✅ 强 | 模板代码 |
| 性能（合批、遮挡、对象池） | ⚠️ 半 | 能写池，瓶颈要 Profiler |
| QA：跑场景断言、修报错 | ✅ 中强 | 有 runtime/debug MCP 时更好 |

Godot 版本说明：[官方文档](https://docs.godotengine.org/en/stable/classes/class_tilemap.html)已将 `TileMap` 标为弃用，推荐 `TileMapLayer`；旧版 Autotile 教程需按项目版本转换为对应的 TileSet 地形工作流。

需要介入的部分：

| 需要你介入的部分 | 你具体要做的事 | 不做会怎样 |
|---|---|---|
| 素材命名与切分约定 | 定好图集规则：帧宽高、哪一行=哪个状态（idle/walk/attack…）、是否 loop、攻击起止帧 | Codex 会乱猜行/帧，动画切错 |
| 物理层 / 碰撞层命名 | 定好 layer 名字与 mask 关系（Player、Enemy、Ground、Hurtbox、Hitbox…） | 层对不上，撞不到或互相穿透 |
| 身体碰撞「手感」 | 开可见碰撞跑几关，拖 Capsule/Rect：脚底缝、贴墙、斜坡 | 卡墙、落空、滑落怪异 |
| 攻击/受击判定对齐 | 对照 attack 帧调攻击方 Hitbox 的启停、位置和大小；多段命中逐段核对；目标 Hurtbox 贴合受击部位 | 打空、穿模、判定早/晚 |
| 动画过渡阈值 | 实机改：落地缓冲、coyote、攻击可否打断、xfade 长短 | 跳→idle 抖、连招僵、手感飘 |
| 玩法条件别全塞动画图 | 复杂判定写在脚本 FSM；Tree 只吃布尔/枚举 | 图难维护，和 Unity 乱拖参数一样 |
| 关卡与 Tile 审美 | 地形规则套用/铺关后自己摆树石建筑、调单向台/半透明平台 | 能跑但关卡难看或碰撞怪 |
| UI / HUD 像素对齐 | 搭好后挪锚点、核对分辨率与安全区 | 糊边、错位 |
| 数值平衡 | 按表试玩改伤害、CD、击退、移速 | 太易/太难，AI 给的只是初值 |
| 美术与特效审美 | 统一调色、光影、粒子密度；定风格基准 | 各物件风格打架 |
| 音频踩帧 | 听脚步/受击/技能是否贴帧，改方法轨时间 | 声画不同步 |
| 性能瓶颈 | 卡时开 Profiler，再让 Codex 改池化/合批 | 人多/特效多时掉帧 |
| 验收闭环 | 每轮：跑场景 → 记 3～5 条手感问题 → 丢回 Codex 改结构 | AI 只堆功能，不收敛手感 |


## 4. 引擎、官方 MCP/Skills 与社区接入

<a id="engines"></a>

核对日期：2026-11-02。下表区分引擎官方资源、工具厂商官方资源、社区资源；文档/示例、Skill、MCP、CLI 是不同交付形态，不能互相替代。以下入口为整理，未在本仓库安装或配置服务。

| 引擎 / 环节 | 来源与身份 | 用途与边界 |
|---|---|---|
| Godot | [官网](https://godotengine.org/) · [官方文档](https://docs.godotengine.org/en/stable/) · [官方示例](https://github.com/godotengine/godot-demo-projects) | 2D/3D 引擎；素材导入、场景、动画、物理以匹配项目版本的文档为准。示例不是 Agent Skill |
| Godot MCP | [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)，**社区** | 启动编辑器、运行项目、获取调试输出及部分场景操作；逐项看工具列表，不能把上表所有能力视为该服务承诺 |
| Godot MCP 另一候选 | [Asset Library 中的 Godot-MCP](https://godotengine.org/asset-library/asset/5245)，作者 IvanMurzak，标注 **Community** | C# 编辑器插件，可连接其云后端或自建服务；上架官方资源库不等于引擎官方出品。本轮未确认 Godot 官方独立 MCP/Skills 发布入口，不将社区项目冠以官方 |
| Unity | [官方手册](https://docs.unity3d.com/Manual/) · [Unity Learn](https://learn.unity.com/) | 继续使用熟悉的 Sprite、Animator、Prefab 管线；许可及支持范围按所用版本核对 |
| Unity 官方 CLI / MCP | [Unity CLI 与 Pipeline 官方教程](https://learn.unity.com/tutorial/6a7e194752fbca26e9ebccbe) | 当前教程说明旧 Assistant 包内 MCP 已弃用，由 Unity CLI 的 `unity mcp` 接替；CLI + Pipeline 驱动编辑器。新旧接入不要混配，兼容版本依官方安装文档 |
| Unity 官方 Skills | [Unity-Technologies/unity-agent-plugin](https://github.com/Unity-Technologies/unity-agent-plugin)（官方教程链接） | 游戏开发与性能优化指导；安装方式按客户端及仓库说明，不把 Claude 插件命令通用于所有客户端 |
| Unreal Engine 官方 MCP | [Epic：Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) | 官方文档标注 **Experimental**；编辑器中启用 Unreal MCP / All Toolsets，适配所用引擎版本。它是 MCP 插件，不能直接称为官方 Skill 包 |
| 像素素材工具官方 Skill / MCP | [Pixelbolt](https://github.com/skulitom/Pixelbolt) | 工具作者提供本地 MCP、CLI 与 Skill；输出 PNG/atlas 等供引擎导入，属于素材工具，不是 Godot/Unity 官方插件 |
| Scenario 官方 MCP / Skills | [Pixel VFX Forge](https://www.scenario.com/explorations/pixel-vfx-forge/) 页面的 [MCP](https://mcp.scenario.com/) / [Skills](https://github.com/scenario-labs/skills) | 工具厂商官方入口，用于素材生产。区分本地 VFX 配方渲染与云端角色/场景生成的费用 |

选型建议（编辑判断）：当前清单偏 2D 像素开发，可沿用 Godot/Unity + PNG 精灵表；先验证素材导入与一个可玩场景，再按实际操作缺口接 MCP。已有引擎项目沿用其版本与管线，不因清单新增入口而迁移。

## 5. 本仓库可用资源与跨用途素材

<a id="local-assets"></a>

- [scenario-pixel-vfx Skill](VFX/scenario-pixel-vfx/SKILL.md)、[ZIP 包](VFX/scenario-pixel-vfx-skill.zip)、[配方格式](VFX/scenario-pixel-vfx/references/recipe.md)、[渲染入口](VFX/scenario-pixel-vfx/scripts/render.mjs)：当前仓库实际携带的资源；其余清单条目主要是外部链接。
- 本地脚本输出 PNG 精灵表、JSON atlas、GIF，可选单帧及带背景预览；没有直接导出 Godot SpriteFrames 的逻辑。网页 Forge 的导出能力与本地脚本分开判断。
- 游戏音效、环境声、角色语音可复用 [Video 音效](Video.md#sfx)和[语音工作室](Video.md#voice)，不再复制维护同一份资源表。
- 游戏 UI、表情、品牌展示可复用 [Video 图标素材](Video.md#icons)；品牌 logo 主要用于介绍/宣传，游戏内部 UI 另按风格选择。
- 像素风游戏宣传片可将精灵帧带入 [Video 工作流](Video.md#workflow)，导出视频时保持像素密度与整数倍缩放。

素材交接建议：固定单帧尺寸、pivot、帧率、循环标记、状态命名、命中帧和碰撞层规范。先在目标引擎跑一个动作，确认切片、透明边缘和声画同步，再批量制作。

## 来源与待核实范围

素材工具能力参照 [Pixelbolt README](https://github.com/skulitom/Pixelbolt)、[Forge 导出说明](https://www.scenario.com/explorations/pixel-vfx-forge/)及[本地源码](VFX/scenario-pixel-vfx/scripts/render.mjs)；combat-vfx-demo 的用途限制参照[上游 LICENSE](https://github.com/yuewen-huang/combat-vfx-demo/blob/main/LICENSE)。个人身份不自动等于非商业用途。

清单未逐项安装实测。缺少仓库链接的 Godot VFX 名称仅保留为检索线索；素材与 Skill 的具体再分发授权需以对应版本的许可为准。
