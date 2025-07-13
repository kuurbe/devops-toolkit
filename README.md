🧰 Mobile DevOps Toolkit

Automated Git commit analysis built entirely in Termux on Android—because who says DevOps can’t be mobile?

🚀 Overview

This lightweight CLI script summarizes Git commit history with total commit count and a preview of recent commits. It's perfect for quick inspections, pipeline previews, or as a starter for a mobile-first CI/CD utility.

Built and committed using only Termux on Android. No laptop. No IDE. Just pure portable hustle.

📦 Features

- 🔍 Total commits + latest 5 messages
- 📁 Fully git-tracked and versioned from mobile
- 🧠 Easily expandable into multi-feature DevOps toolkit
- ✅ Ready to integrate with GitHub Actions, Slack alerts, API scraping, and more

💻 Usage

Run inside any Git repository:

`bash
python commit_summary.py
`

Output sample:
`
Total commits: 17
Recent commits:
 - b12f8a2 Fix deployment YAML typo
 - 82e1d41 Add webhook parser
 - 31a4c7a Initial commit with commit summary tool
...
`

🌍 Made With

- Termux (Android)
- Python
- Git CLI

🙌 Credits

Created by @kuurbe  
Built from the ground up in Termux 💥

🛠️ Next Steps

- 🔧 Add GitHub API integration
- 🟢 Include build status checker
- 💬 Push Slack or email notifications
- 📊 Generate Markdown reports for pipelines

---

Feel free to fork, contribute, or remix for your own workflow. DevOps is where you take it.
`

---
