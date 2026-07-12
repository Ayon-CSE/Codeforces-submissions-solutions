<div align="center">

# Codeforces Submissions Archive

</div>

<div align="center">

[![Codeforces](https://badges.joonhyung.xyz/codeforces/Ayon.svg)](https://codeforces.com/profile/Ayon)
[![GitHub Actions](https://img.shields.io/badge/automation-GitHub%20Actions-2088FF?logo=github-actions)](../../actions/workflows/harwest.yml)

**Automatically archive your Codeforces submissions**

> **Featuring full problem ratings, contest names, and all submission verdicts!**
>
> All your Codeforces submissions are automatically fetched daily with complete details including problem difficulty, full contest information, and submission verdicts (AC, WA, TLE, CE, etc.).

</div>

---

## 📊 Statistics

| Platform                                              | Total Submissions                     | **Accepted (AC)**                              |
| ----------------------------------------------------- | ------------------------------------- | ---------------------------------------------- |
| **[Codeforces](https://codeforces.com/profile/Ayon)** | **[5005](submissions/codeforces.md)** | **[2259](submissions/codeforces_accepted.md)** |

---

## 🎯 View Submissions

### Codeforces

- **[📋 View All Submissions (5005) →](submissions/codeforces.md)** - **Complete list of ALL submissions** including accepted, wrong answer, TLE, CE, and more
- **[✅ View Accepted Solutions (2259) →](submissions/codeforces_accepted.md)** - **Only accepted solutions** (OK verdict) with ratings and contest names
- **[👤 View Codeforces Profile →](https://codeforces.com/profile/Ayon)** - Check profile on Codeforces

Each submission includes:

- ✅ Problem name and difficulty rating
- ✅ Full contest name with division
- ✅ Submission date
- ✅ Verdict status (✅ OK, ❌ WA, ⏱️ TLE, 🔴 CE, etc.)
- ✅ Direct link to submission on Codeforces

---

## 🚀 How It Works

- GitHub Actions automatically fetches submissions **every 6 hours**
- New submissions are automatically merged with existing data
- Changes are automatically committed and pushed to GitHub
- Markdown tables are regenerated with the latest data

---

## 📝 Configuration

The script is configured in `fetch_submissions.py`:

- Username: `Ayon`
- API: Codeforces API v2
- Fetch frequency: Daily at 12:00 AM UTC via GitHub Actions

---

## 🚀 How It Works

This repository automatically fetches your **accepted solutions only** from Codeforces every day using GitHub Actions and the official Codeforces API.

### Features

- **Automatic Daily Updates**: Runs every day at 12:00 AM UTC
- **Complete Details**: Problem ratings and full contest names
- **Direct Links**: Click to view any solution on Codeforces
- **JSON Backup**: All submission data stored for analysis
- **Zero Maintenance**: Fully automated via GitHub Actions

### Workflow

```
fetch_submissions.py → Fetch Codeforces API → Filter AC Solutions →
Generate Markdown with Ratings → Auto-commit → Push to GitHub
```

---

## 📁 Repository Structure

```
📦 Codeforces-Submissions/
├── 📄 README.md                        # This file
├── 📄 fetch_submissions.py             # Main fetch script
├── 📂 .github/workflows/
│   └── 📄 harwest.yml                  # GitHub Actions automation
├── 📂 config/
│   ├── 📄 users.json                   # Username configuration
│   └── 📄 README.md                    # Configuration guide
└── 📂 submissions/
    ├── 📄 codeforces_accepted.md       # All AC solutions with ratings
    ├── 📄 state.json                   # Fetch state tracking
    └── 📂 codeforces/
        ├── 📄 codeforces_submissions.json
        └── 📄 codeforces_accepted_submissions.json
```

---

## ⚙️ Configuration

Edit `config/users.json` to change the Codeforces username:

```json
{
  "codeforces": ["Ayon"]
}
```

For more details: [config/README.md](config/README.md)

---

## 🔥 Manual Trigger

Want to fetch accepted solutions immediately?

1. Go to [Actions](../../actions) tab
2. Select **"Fetch Codeforces Submissions"**
3. Click **"Run workflow"**

---

## 📈 What's Included

### Codeforces - All Submissions

| Column     | Details                                |
| ---------- | -------------------------------------- |
| Problem    | Problem name                           |
| Rating     | Problem difficulty (800-3500+)         |
| Contest    | Full contest name with division        |
| Verdict    | Submission result (OK, WA, TLE, CE...) |
| Date       | Submission date                        |
| Submission | Direct link to Codeforces submission   |

### Codeforces - Accepted Solutions Only

| Column   | Details                              |
| -------- | ------------------------------------ |
| Problem  | Problem name                         |
| Rating   | Problem difficulty (800-3500+)       |
| Contest  | Full contest name with division      |
| Date     | Submission date                      |
| Solution | Direct link to Codeforces submission |

---

## 💡 About

This repository automatically displays all your **Codeforces submissions** with:

- **All Submissions (4857)**: Every submission with verdict status (accepted, wrong answer, TLE, CE, etc.)
- **Accepted Only (2181)**: Filtered list of only accepted solutions
- Problem difficulty ratings
- Full contest names and divisions
- Direct links to each submission
- Complete submission metadata

Perfect for:

- Building a competitive programming portfolio
- Tracking your problem-solving progress and learning journey
- Analyzing your submission patterns and verdict distribution
- Easy reference to all past attempts
- Showcase your skills and problem-solving growth

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
