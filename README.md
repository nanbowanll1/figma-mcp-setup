# figma-mcp-setup

A [Claude Code Skill](https://docs.anthropic.com/en/docs/claude-code) that helps you configure the [figma-developer-mcp](https://github.com/nicolo-figma/figma-developer-mcp) server for Claude Code, enabling Claude to interact with Figma designs directly.

## Features

- Step-by-step guide to obtain Figma API Key
- Automatic API Key validation before configuration
- Cross-platform MCP server configuration (Windows / macOS / Linux)
- Connection testing and troubleshooting

## Installation

1. Download or clone this repository
2. Copy the `figma-mcp-setup` folder to your Claude Code skills directory:

   | Platform | Path |
   |----------|------|
   | Windows | `C:\Users\<username>\.claude\skills\` |
   | macOS/Linux | `~/.claude/skills/` |

3. Restart Claude Code

## Usage

Once installed, trigger the skill by telling Claude:

- "Help me configure Figma MCP"
- "Set up Figma integration"
- "Connect Claude to Figma"

Claude will guide you through:

1. **Obtaining an API Key** - Step-by-step instructions for generating a Figma Personal Access Token
2. **Validating the Key** - Automatic verification that your API Key works
3. **Configuring MCP** - Writing the correct configuration to your `.claude.json`
4. **Testing the Connection** - Verifying everything works end-to-end

## Skill Structure

```
figma-mcp-setup/
├── SKILL.md                        # Main skill instructions
├── README.md                       # This file
├── scripts/
│   └── validate_figma_key.py       # API Key validation script
└── references/
    └── get_api_key_guide.md        # Detailed API Key guide
```

## Prerequisites

- [Node.js](https://nodejs.org/) and npm installed
- A [Figma](https://www.figma.com/) account
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed

## Available MCP Tools After Setup

Once configured, Claude gains access to:

| Tool | Description |
|------|-------------|
| `get_figma_data` | Fetch file layout, content, visuals, and component info |
| `download_figma_images` | Download SVG/PNG images from Figma files |

## License

MIT
