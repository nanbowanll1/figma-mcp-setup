# How to Get Figma API Key

## Step-by-Step Guide

### Step 1: Log in to Figma

Open [figma.com](https://www.figma.com) and log in to your account.

### Step 2: Open Account Settings

1. Click your profile avatar in the top-right corner
2. Select **Settings** from the dropdown menu

### Step 3: Navigate to Security Tab

In the Settings page, click the **Security** tab in the left sidebar.

### Step 4: Generate Personal Access Token

1. Scroll down to the **Personal access tokens** section
2. Click **Generate new token**
3. Enter a descriptive name for your token (e.g., "Claude MCP Integration")
4. Click **Generate token**

### Step 5: Copy Your Token

**Important:** Copy the token immediately! It will only be shown once.

The token format looks like: `figd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 6: Store Safely

- Never share your API key publicly
- Do not commit it to version control
- Store it in environment variables or secure configuration files

## Token Permissions

Personal access tokens have the same permissions as your Figma account:
- Read access to files you can view
- Write access to files you can edit
- Access to team resources based on your team membership

## Troubleshooting

### Token Not Working?

1. **Expired token**: Tokens may expire. Generate a new one if needed.
2. **Revoked token**: Check if the token was revoked in Settings > Security.
3. **Wrong token**: Ensure you copied the complete token without extra spaces.

### Rate Limits

Figma API has rate limits. If you encounter 429 errors, wait before retrying.

## Reference Links

- [Figma API Documentation](https://www.figma.com/developers/api)
- [Authentication Guide](https://www.figma.com/developers/api#authentication)
