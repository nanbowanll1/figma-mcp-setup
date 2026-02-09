# figma-mcp-setup

一个 [Claude Code Skill](https://docs.anthropic.com/en/docs/claude-code)，帮助你配置 [figma-developer-mcp](https://github.com/nicolo-figma/figma-developer-mcp) 服务器，让 Claude 能够直接读取和操作 Figma 设计文件。

[English](./README.md)

## 功能特性

- 逐步引导获取 Figma API Key
- 配置前自动验证 API Key 有效性
- 跨平台 MCP 服务器配置（Windows / macOS / Linux）
- 连接测试与故障排查

## 安装方法

1. 下载或克隆本仓库：

   ```bash
   git clone https://github.com/nanbowanll1/figma-mcp-setup.git
   ```

2. 将 `figma-mcp-setup` 文件夹复制到 Claude Code skills 目录：

   | 平台 | 路径 |
   |------|------|
   | Windows | `C:\Users\<用户名>\.claude\skills\` |
   | macOS/Linux | `~/.claude/skills/` |

   或直接一步到位：

   ```bash
   # macOS/Linux
   git clone https://github.com/nanbowanll1/figma-mcp-setup.git ~/.claude/skills/figma-mcp-setup

   # Windows (PowerShell)
   git clone https://github.com/nanbowanll1/figma-mcp-setup.git "$env:USERPROFILE\.claude\skills\figma-mcp-setup"
   ```

3. 重启 Claude Code

## 使用方法

安装完成后，在 Claude Code 中说：

- "帮我配置 Figma MCP"
- "设置 Figma 集成"
- "连接 Claude 到 Figma"

Claude 会引导你完成以下步骤：

1. **获取 API Key** - 逐步指导你在 Figma 平台生成 Personal Access Token
2. **验证 Key** - 自动检测 API Key 是否有效
3. **配置 MCP** - 将正确的配置写入 `.claude.json`
4. **测试连接** - 验证 Figma MCP 是否连接成功

## 目录结构

```
figma-mcp-setup/
├── SKILL.md                        # Skill 主指令文件
├── README.md                       # 英文文档
├── README_CN.md                    # 中文文档
├── scripts/
│   └── validate_figma_key.py       # API Key 验证脚本
└── references/
    └── get_api_key_guide.md        # API Key 获取详细教程
```

## 前置条件

- 已安装 [Node.js](https://nodejs.org/) 和 npm
- 拥有 [Figma](https://www.figma.com/) 账号
- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI

## 配置成功后可用的 MCP 工具

配置完成后，Claude 将获得以下能力：

| 工具 | 说明 |
|------|------|
| `get_figma_data` | 获取 Figma 文件的布局、内容、视觉和组件信息 |
| `download_figma_images` | 从 Figma 文件中下载 SVG/PNG 图片 |

## 许可证

MIT
