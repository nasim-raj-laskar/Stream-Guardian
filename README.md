![github-submission-banner](https://github.com/user-attachments/assets/a1493b84-e4e2-456e-a791-ce35ee2bcf2f)

# 🚀 StreamGuardian

> Real-time toxic comment detection dashboard powered by Fluvio and Groq

---

## 📌 Problem Statement

**Problem Statement 1 - Weave Al magic with Groq**

---

## 🎯 Objective

In fast-moving online platforms like live streams, group chats, and comment feeds, toxic behavior such as harassment, hate speech, and abuse often goes unchecked due to the sheer volume of content.

**StreamGuardian** solves this problem by offering:
- Real-time detection of toxic messages
- Visual analytics to identify patterns
- Filtering tools to isolate toxic content for moderation

It empowers moderators and platforms to maintain healthy digital spaces.

---

## 🧠 Team & Approach

### Solo Developer :  
- [Nasim Raj Laskar](https://github.com/nasim-raj-laskar) 

### Approach:
- Chose this problem for its **high social impact** in today’s digital world.
- Tackled the **real-time challenge** by combining Fluvio with Groq's lightning-fast inference.
- Focused heavily on **dashboard usability** for moderators.
- Iterated on design to make filtering, flagging, and downloading effortless.

---

## 🛠️ Tech Stack

### Core Technologies Used:
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Backend:** Flask (Python), Flask-SocketIO  
- **Database:** In-memory Python storage (for demo), optionally Redis  
- **APIs:** Groq API for toxic comment prediction  
- **Hosting:** Render (Backend + Frontend)

### Sponsor Technologies Used:
- ✅ **Groq:** Used Groq’s API for ultra-low-latency toxicity classification  
- ✅ **Fluvio:** Integrated real-time data stream from Fluvio broker into the backend consumer  
- [ ] **Monad:**  
- [ ] **Base:**  
- [ ] **Screenpipe:**  
- [ ] **Stellar:**  

---

## ✨ Key Features

- ✅ **Real-Time Detection**: Instantly flags toxic messages as they are streamed  
- ✅ **Toxicity Dashboard**: Clean vs toxic stats, donut charts, line graphs  
- ✅ **WebSockets**: Auto-refreshing UI without needing reload  
- ✅ **Export Support**: CSV download for logs, PNG/SVG export for graphs  
- ✅ **Filter Tabs**: Toggle between All / Clean / Toxic messages  
- ✅ **Emoji Flagging**: ⚠️ emojis clearly mark toxic content  

---

## 📽️ Demo & Deliverables

- **Demo Video Link:** [https://youtu.be/demo-link](https://youtu.be/demo-link)  
- **Pitch Deck / PPT Link:** [https://docs.google.com/presentation/d/streamguardian-ppt](https://docs.google.com/presentation/d/streamguardian-ppt)

---

## ✅ Tasks & Bonus Checklist

- ✅ **All members followed required social channels and submitted the form**  
- ✅ **Bonus Task 1 - Badges shared & form submitted (2 points)**  
- ✅ **Bonus Task 2 - Signed up for Sprint.dev & submitted form (3 points)**

---

## 🧪 How to Run the Project

### Requirements:
- Python 3.10+  
- Node.js (for frontend testing if needed)  
- Groq API Key  
- Fluvio CLI (with local topic setup)

### Local Setup:
```bash
# Clone the repo
git clone https://github.com/bitbenders/streamguardian

# Backend setup
cd streamguardian/dashboard
pip install -r requirements.txt

# Run the Flask server
python app.py
```

Optional:
- Set up `.env` for Groq API key
- Use Fluvio to publish sample messages to topic

---

## 🧬 Future Scope

- ☁️ Host on cloud (AWS/GCP) with Redis backend  
- 👥 Add user roles (moderator/admin)  
- 🌍 Multilingual toxicity detection support  
- 🤖 Add emotional tone and sentiment analysis  
- 🔌 Plug-ins for platforms like Discord, Twitch, Slack  
- 📱 Convert dashboard into a mobile-friendly PWA

---

## 📎 Resources / Credits

- Groq API Docs  
- Fluvio Streaming Platform  
- Flask & Flask-SocketIO  
- Chart.js for dashboard visuals  
- Toxic comment dataset from Kaggle  
- Inspiration from Google’s Perspective API

---

## 🏁 Final Words

StreamGuardian was born from a passion to make online spaces safer.  
We brainstormed hard, pivoted tech stacks twice, and learned to stream and predict in real time!  
Huge thanks to the mentors and organizers 🙌

---
