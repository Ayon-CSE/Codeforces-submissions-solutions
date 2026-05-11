<div align="center">

# Competitive Programming Archive

</div>

<div align="center">

[![Codeforces](https://badges.joonhyung.xyz/codeforces/Ayon.svg)](https://codeforces.com/profile/Ayon)
[![AtCoder](https://badges.joonhyung.xyz/atcoder/AyonCoder.svg)](https://atcoder.jp/users/AyonCoder)
[![GitHub Actions](https://img.shields.io/badge/automation-GitHub%20Actions-2088FF?logo=github-actions)](../../actions/workflows/harwest.yml)

**Automatically archive your competitive programming submissions from Codeforces & AtCoder**

> **NEW!** For all your harvesting needs, use the magical `harwest_control_panel.bat` (the one batch to rule them all)! It's so powerful, even your submissions are afraid to be left behind. Run it, and let the automation wizardry begin!
>
> **v2.0** System upgraded with enhanced automation and improved user experience!

</div>

---

## 🚀 Quick Start

> **Want this for your own profile?**  
> **📖 [Complete User Guide](USER_GUIDE.md)** - Setup in 5 minutes!

**Fork this repository**, then run:
```bash
python fresh_start.py
```

That's it! Your submissions will be automatically harvested daily via GitHub Actions.

---

<div align="center">

## 📊 My Submissions

</div>

<div align="center">

### 🎯 Platforms

| Platform | Profile | Solutions | Submissions |
|----------|---------|-----------|-------------|
| **Codeforces** | [Ayon](https://codeforces.com/profile/Ayon) | [![Codeforces](https://badges.joonhyung.xyz/codeforces/Ayon.svg)](https://codeforces.com/profile/Ayon) | [📝 View All](codeforces.md) |
| **AtCoder** | [AyonCoder](https://atcoder.jp/users/AyonCoder) | [![AtCoder](https://badges.joonhyung.xyz/atcoder/AyonCoder.svg)](https://atcoder.jp/users/AyonCoder) | [📝 View All](atcoder.md) |

</div>

---

### 📁 Repository Structure

<details>
<summary>Click to expand repository structure</summary>

```
📦 Codeforces_Atcoder-submissions/
├── 📄 codeforces.md              # Codeforces submissions table
├── 📄 atcoder.md                 # AtCoder submissions table
├── 📂 submissions/
│   ├── 📂 codeforces/
│   │   └── 📂 [contest_id]/
│   │       └── 📄 [problem_code].[ext]
│   ├── 📂 atcoder/
│   │   └── 📂 [contest_id]/
│   │       └── 📄 [problem_code].[ext]
│   └── 📄 submissions.json       # Metadata database
├── 📂 config/
│   └── 📄 users.json             # Username configuration
└── 📄 fresh_start.py             # Setup script
```

</details>

---

## ⚙️ How It Works

<details>
<summary>Click to expand how it works</summary>

### 🤖 Automated Daily Harvesting

GitHub Actions runs **every day at 11:00 PM BDT (5:00 PM UTC)**:
- ✅ **Smart Scanning**: Checks last 30 days for new submissions (fast & efficient)
- ✅ **Full History**: First run fetches all submissions with `--full-scan`
- ✅ **Auto Updates**: Tags and ratings update automatically when changed
- ✅ **Fallback Links**: Creates platform links when code fetch fails
- ✅ **Smart Scheduling**: Monthly check if repository inactive >30 days

### 🔧 Features

- **Zero Maintenance**: Fully automated via GitHub Actions
- **Multi-Platform**: Supports Codeforces and AtCoder
- **Multi-Account**: Track multiple usernames per platform
- **Smart Updates**: Only checks recent submissions (configurable)
- **Metadata Updates**: Auto-detects rating/tag changes
- **Profile Contributions**: Shows as GitHub activity (with proper git config)
- **Private Support**: Works with private repositories

</details>

---

## 📖 Documentation

- **[📖 User Guide](USER_GUIDE.md)** - Complete setup & usage documentation
- **[⚙️ Configuration](config/README.md)** - Username configuration details
- **[🔄 Workflow](.github/workflows/harwest.yml)** - GitHub Actions automation

---

## 🔥 Manual Trigger

Want to run immediately or do a full scan?

1. Go to [**Actions**](../../actions/workflows/harwest.yml) tab
2. Click **"Harwest Submissions"** → **"Run workflow"**
3. Select options:
   - ✅ **Full scan** - Fetch complete history
   - ⚡ **Check recent** - Last 30 days only (default)
4. Click **"Run workflow"**

---

## 💡 About This Repository

This repository uses [**Harwest**](https://github.com/nileshsah/harwest-tool) to automatically fetch and archive competitive programming submissions. All submissions are stored with proper timestamps, organized by contest, and presented in clean markdown tables.

**Benefits:**
- 📈 Track your competitive programming journey
- 🌐 Showcase your solutions publicly
- 📊 Build a comprehensive coding portfolio
- 🎯 Never lose your solutions
- 🔍 Easy search and navigation

---

## 🆘 Need Help?

- 📖 Read the [User Guide](USER_GUIDE.md)
- 🐛 Check [Issues](../../issues)
- 💬 See [Actions logs](../../actions) for workflow details
- ⭐ Star the [original project](https://github.com/nileshsah/harwest-tool)

---

<div align="center">

**Last automated harvest:** _Check [Actions](../../actions) for latest run_

Built with ❤️ by [Ayon Das Gupta](https://github.com/Ayon-CSE) using [Harwest](https://github.com/nileshsah/harwest-tool)

</div>

<br>
<p align="center"><sub>V2.0</sub></p>
