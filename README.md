# 🧑‍💼 Automated HR Job Applicant Pipeline — n8n

An end-to-end HR recruitment automation workflow built with n8n that triggers on new Google Form submissions, sends confirmation emails to applicants, and notifies the HR team on Slack in real time.

---

## 📌 Project Overview

Manually handling job applications is slow and error-prone. This workflow automates the entire process — the moment a candidate submits a job application form, the system instantly processes it, emails the candidate, and alerts the HR team on Slack.

**Result:** Reduced manual HR processing time by 100%.

---

## ⚙️ Workflow

```
Google Sheets Trigger (new form submission)
        ↓
Send Email (confirmation to applicant via Gmail)
        ↓
Slack (notify HR team in #new-applications channel)
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| n8n | Workflow automation |
| Google Forms | Job application form |
| Google Sheets | Store form responses |
| Gmail SMTP | Send confirmation email to applicant |
| Slack API | Notify HR team instantly |

---

## 📋 Features

- ✅ Auto-triggers when a new application is submitted
- ✅ Sends instant confirmation email to the applicant
- ✅ Notifies HR team on Slack with full applicant details
- ✅ Stores all applications in Google Sheets automatically
- ✅ Fully automated — zero manual work required

---

## 🚀 Setup Instructions

### Prerequisites
- n8n installed locally or on a server
- Google account (Gmail + Google Sheets + Google Forms)
- Slack workspace with a channel for HR notifications

### Step 1 — Clone this repository
```bash
git clone https://github.com/yourusername/n8n-hr-applicant-pipeline.git
cd n8n-hr-applicant-pipeline
```

### Step 2 — Import workflow into n8n
1. Open n8n at `http://localhost:5678`
2. Click **"+"** to create new workflow
3. Click **"..."** menu → **"Import from File"**
4. Select `workflow.json` from this repository

### Step 3 — Set up Google Form
Create a Google Form with these fields:
- Full Name
- Email Address
- Phone Number
- Position Applied For
- Years of Experience

Link the form responses to a Google Sheet.

### Step 4 — Configure Credentials
Replace the following placeholders with your own credentials in n8n:

```
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GMAIL_SMTP_USER=your_gmail@gmail.com
GMAIL_SMTP_PASSWORD=your_16_char_app_password
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
```

### Step 5 — Activate the workflow
Toggle the workflow to **Active** in n8n and submit a test form entry.

---

## 📧 Email Template

```
Dear [Applicant Name],

Thank you for applying for the [Position] role.
We have received your application and will review it shortly.
We will contact you within 3-5 business days.

Best regards,
HR Team
```

---

## 💬 Slack Notification

```
🆕 New Job Application Received!

👤 Name: [Full Name]
📧 Email: [Email Address]
📞 Phone: [Phone Number]
💼 Position: [Position Applied For]
📅 Experience: [Years] years

Please review the application!
```

---

## 📁 Project Structure

```
n8n-hr-applicant-pipeline/
│
├── workflow.json        # n8n workflow (credentials removed)
├── .env.example         # Required credentials template
├── .gitignore           # Ignored files
└── README.md            # Project documentation
```

---

## 🔐 Security Note

All credentials have been removed from `workflow.json`.
Never upload real credentials to GitHub.
Use `.env.example` as a reference to set up your own credentials.

---

## 👨‍💻 Author

**Khansa Malik**
AI Engineer Intern @ CarbonRepro
Skills:Gen AI . AI Agents . LLM . RAG . n8n · Python ·  Workflow Automation

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
