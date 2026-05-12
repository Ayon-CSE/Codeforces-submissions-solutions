<div align="center">

# Competitive Programming Archive

</div>

<div align="center">

[![Codeforces](https://badges.joonhyung.xyz/codeforces/Ayon.svg)](https://codeforces.com/profile/Ayon)
[![AtCoder](https://badges.joonhyung.xyz/atcoder/AyonCoder.svg)](https://atcoder.jp/users/AyonCoder)
[![GitHub Actions](https://img.shields.io/badge/automation-GitHub%20Actions-2088FF?logo=github-actions)](../../actions/workflows/fetch_accepted.yml)

**Automatically archive your competitive programming accepted solutions from Codeforces & AtCoder**

> **Featuring full problem ratings and contest names!**
>
> Your accepted solutions are automatically fetched daily with complete details including problem difficulty and full contest information.

</div>

---

## 📊 Statistics

| Platform       | Total Submissions                 | **Accepted (AC)**                              |
| -------------- | --------------------------------- | ---------------------------------------------- |
| **Codeforces** | [4851](submissions/codeforces.md) | **[2177](submissions/codeforces_accepted.md)** |
| **AtCoder**    | -                                 | -                                              |

---

## 🎯 View Accepted Solutions

### Codeforces - 2177 Accepted Solutions

Each solution includes:

- ✅ Problem name and difficulty rating
- ✅ Full contest name with division
- ✅ Submission date
- ✅ Direct link to solution on Codeforces

**[👉 View All Codeforces Solutions →](submissions/codeforces_accepted.md)**

### AtCoder

AtCoder submissions coming soon (username verification in progress)

**[View AtCoder Solutions →](submissions/atcoder_accepted.md)**

---

## 🚀 How It Works

This repository automatically fetches your **accepted solutions only** from Codeforces and AtCoder every day using GitHub Actions and the official APIs.

### Features

- **Automatic Daily Updates**: Runs at 11:00 PM BDT (5:00 PM UTC)
- **Complete Details**: Problem ratings and full contest names
- **Direct Links**: Click to view any solution on the platform
- **JSON Backup**: All submission data stored for analysis
- **Zero Maintenance**: Fully automated via GitHub Actions

### Workflow

```
fetch_submissions.py → Fetch API Data → Filter AC Solutions →
Generate Markdown with Ratings → Auto-commit → Push to GitHub
```

---

## 📁 Repository Structure

```
📦 Codeforces_Atcoder-submissions/
├── 📄 README.md                        # This file
├── 📄 fetch_submissions.py             # Main fetch script
├── 📂 .github/workflows/
│   └── 📄 fetch_accepted.yml           # GitHub Actions automation
├── 📂 config/
│   ├── 📄 users.json                   # Username configuration
│   └── 📄 README.md                    # Configuration guide
└── 📂 submissions/
    ├── 📄 codeforces_accepted.md       # All AC solutions with ratings
    ├── 📄 atcoder_accepted.md          # All AC solutions
    ├── 📂 codeforces/
    │   ├── 📄 codeforces_submissions.json
    │   └── 📄 codeforces_accepted_submissions.json
    └── 📂 atcoder/
        ├── 📄 atcoder_submissions.json
        └── 📄 atcoder_accepted_submissions.json
```

---

## ⚙️ Configuration

Edit `config/users.json` to change usernames:

```json
{
  "codeforces": ["Ayon"],
  "atcoder": ["AyonCoder"]
}
```

For more details: [config/README.md](config/README.md)

---

## 🔥 Manual Trigger

Want to fetch accepted solutions immediately?

1. Go to [Actions](../../actions) tab
2. Select **"Fetch Accepted Solutions"**
3. Click **"Run workflow"**

---

## 📈 What's Included

### Codeforces Solutions

| Column   | Details                              |
| -------- | ------------------------------------ |
| Problem  | Problem name                         |
| Rating   | Problem difficulty (800-3500+)       |
| Contest  | Full contest name with division      |
| Date     | Submission date                      |
| Solution | Direct link to Codeforces submission |

---

## 💡 About

This repository automatically displays all your **accepted solutions** with:

- Problem difficulty ratings
- Full contest names and divisions
- Direct links to each solution
- Complete submission metadata

Perfect for:

- Building a competitive programming portfolio
- Tracking your problem-solving progress
- Easy reference to past solutions
- Showcase your skills

---

<div align="center">

**Last updated:** Check [Actions](../../actions) for latest run

Built with ❤️ by [Ayon Das Gupta](https://github.com/Ayon-CSE)

</div>

<br>
<p align="center"><sub>V1.0 - Automated Accepted Solutions Archive</sub></p>

</div>

<br>
<p align="center"><sub>V2.0</sub></p>
