# 🚀 StreamGuardian

> Real-time toxic comment detection dashboard powered by Fluvio and Groq

## 🎯 Objective

In fast-moving online platforms like live streams, group chats, and comment feeds, toxic behavior such as harassment, hate speech, and abuse often goes unchecked due to the sheer volume of content.

**StreamGuardian** solves this problem by offering:
- Real-time detection of toxic messages
- Visual analytics to identify patterns
- Filtering tools to isolate toxic content for moderation

It empowers moderators and platforms to maintain healthy digital spaces.

---

## 🛠️ Tech Stack

### Core Technologies Used:
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Backend:** Flask (Python), Flask-SocketIO
- **Streaming** Fluvio Python SDK
- **APIs:** Groq API for toxic comment prediction  
- **Hosting:** Render (Backend + Frontend)

### Technologies Used:
- ✅ **Groq:** Used Groq’s API for ultra-low-latency toxicity classification  
- ✅ **Fluvio:** Integrated real-time data stream from Fluvio broker into the backend consumer  

---

## ✨ Key Features

- ✅ **Real-Time Detection**: Instantly flags toxic messages as they are streamed  
- ✅ **Toxicity Dashboard**: Clean vs toxic stats, donut charts, line graphs  
- ✅ **WebSockets**: Auto-refreshing UI without needing reload  
- ✅ **Export Support**: CSV download for logs, PNG/SVG export for graphs  
- ✅ **Filter Tabs**: Toggle between All / Clean / Toxic messages  
- ✅ **Emoji Flagging**: ⚠️ emojis clearly mark toxic content  
![dashboard](https://github.com/nasim-raj-laskar/Stream-Guardian/blob/main/img/Screenshot%202025-04-20%20211204.png)
---

## 🧪 How to Run the Project

### Requirements:
- Operating System: Linux or macOS (WSL2 supported on Windows)
- Rust toolchain: Rust 1.56 or newer
- curl: For installation
- Python 3.10+    
- Groq API Key  
- Fluvio CLI (with local topic setup)

### Local Setup:
```bash
# Clone the repo
https://github.com/nasim-raj-laskar/Stream-Guardian.git

#install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

#reload the shell
source $HOME/.cargo/env

#install Fluvio CLI
curl -fsSL https://packages.fluvio.io/v1/install.sh | bash

#Add to your path
export PATH="$HOME/.fluvio/bin:$PATH"

#install fluvio python sdk
pip install fluvio

#Start a local clustor
fluvio cluster start --local

#Create the topic names "chat-room"
fluvio topic create chat-room

#Run the Fluvio producer for comments streaming
python3 -m streamm.producer

# Backend setup
#Install dependencies
pip install flask flask-socketio eventlet

# Run the Flask server
python3 -m dashboard.app
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

