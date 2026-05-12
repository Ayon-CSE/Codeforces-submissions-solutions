# Configuration Guide

## Users Configuration

Edit `users.json` to add your Codeforces username:

```json
{
  "codeforces": ["username1", "username2"]
}
```

### Current Configuration

- **Codeforces**: Ayon

## How to Update Username

1. Edit `config/users.json`
2. Update the username(s) in the codeforces array
3. Commit and push to trigger the workflow
4. GitHub Actions will fetch submissions automatically

## Workflow

The GitHub Actions workflow runs:
- **Automatically**: Every day at 12:00 AM UTC
- **Manually**: Go to Actions → Run workflow

### Workflow Features

- Fetches submissions from your Codeforces profile
- Filters accepted (AC) solutions only
- Generates markdown table with problem ratings
- Automatically commits and pushes changes
- No additional configuration needed!
