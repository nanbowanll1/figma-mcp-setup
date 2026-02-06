---
name: figma-mcp-setup
description: Configure figma-developer-mcp server for Claude Code. This skill should be used when the user wants to set up Figma MCP integration, configure Figma API access, or troubleshoot Figma MCP connection issues. Triggers include "configure Figma MCP", "set up Figma integration", or "connect Claude to Figma".
---

# Figma MCP Setup

This skill guides users through configuring the figma-developer-mcp server for Claude Code, enabling Claude to interact with Figma designs directly.

## Prerequisites

- Node.js and npm installed
- A Figma account
- Claude Code CLI installed

## Configuration Workflow

### Phase 1: Obtain Figma API Key

If the user does not have an API Key, direct them to the guide:

1. Read `references/get_api_key_guide.md` for detailed instructions
2. Key steps: Figma Settings > Security > Personal access tokens > Generate new token
3. Token format: `figd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Phase 2: Validate API Key

Before configuring, validate the API Key to prevent connection issues:

```bash
# Windows
py -3 scripts/validate_figma_key.py <API_KEY>

# macOS/Linux
python3 scripts/validate_figma_key.py <API_KEY>
```

Expected output for valid key:
```json
{
  "valid": true,
  "message": "API Key is valid",
  "user": {
    "id": "...",
    "email": "...",
    "handle": "..."
  }
}
```

If validation fails, guide the user to regenerate the token.

### Phase 3: Configure MCP Server

Add the following configuration to the user's Claude configuration file.

**Configuration file locations:**
- Project-level: `.claude.json` in project root
- User-level: `~/.claude.json` (Windows: `C:\Users\<username>\.claude.json`)

**Configuration template:**

```json
{
  "mcpServers": {
    "figma": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "figma-developer-mcp",
        "--stdio"
      ],
      "env": {
        "FIGMA_API_KEY": "<USER_API_KEY>"
      }
    }
  }
}
```

**Platform-specific commands:**

| Platform | command | args prefix |
|----------|---------|-------------|
| Windows | `cmd` | `["/c", "npx", ...]` |
| macOS/Linux | `npx` | `["-y", "figma-developer-mcp", "--stdio"]` |

### Phase 4: Test MCP Connection

After configuration, verify the connection:

1. Restart Claude Code to reload MCP configuration
2. Test with a simple Figma operation:
   - Ask Claude to fetch data from a Figma file
   - Example: "Get the structure of this Figma file: [Figma URL]"

**Available MCP Tools after setup:**
- `mcp__figma__get_figma_data` - Fetch file layout, content, and component info
- `mcp__figma__download_figma_images` - Download SVG/PNG images from Figma

## Troubleshooting

### Connection Failed

1. **Verify API Key**: Run `validate_figma_key.py` again
2. **Check npx**: Ensure `npx` is available in PATH
3. **Network**: Confirm access to api.figma.com

### MCP Not Loading

1. **JSON syntax**: Validate configuration file is valid JSON
2. **Restart required**: Claude Code must be restarted after config changes
3. **File location**: Ensure config file is in correct location

### Permission Errors

1. **File access**: Check Figma file is accessible with your account
2. **Token scope**: Personal tokens inherit your account permissions

## Quick Setup Checklist

- [ ] Figma API Key obtained from Settings > Security
- [ ] API Key validated with `validate_figma_key.py`
- [ ] Configuration added to `.claude.json`
- [ ] Claude Code restarted
- [ ] Test connection with a Figma file URL
