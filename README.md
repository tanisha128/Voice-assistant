# 🎙️ AI Voice Assistant (Python)

A smart voice-controlled assistant built using Python that can perform tasks like opening websites, telling time/date, playing music, and responding to user commands using speech recognition and text-to-speech.

## 🚀 Features

* 🎤 Voice Command Recognition
* 🔊 Text-to-Speech Responses
* 🌐 Open Websites (Google, YouTube, Facebook)
* ⏰ Tell Current Time
* 📅 Tell Today’s Date
* 🎵 Play Songs from YouTube
* 🌦️ Weather Information (API-based)
* ❌ Exit Command Support

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* pywhatkit (YouTube playback)
* Requests (API calls)
* Datetime


## 📂 Project Structure

```
├── main.py          # Main voice assistant script
├── requirements.txt # Dependencies



## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/tanisha128/Voice-assistant.git
cd Javaris
```

2. Create virtual environment:

```bash
python -m venv .venv
```

3. Activate virtual environment:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

Then speak commands like:

* "Open Google"
* "What is the time"
* "Play song name"
* "What is today's date"
* "Weather in Pune"
* "Stop"

---

## 🌦️ Weather API Setup

This project uses OpenWeather API.

1. Sign up at: https://openweathermap.org
2. Get your API key
3. Replace in code:

```python
api_key = "YOUR_API_KEY"
```

---

## 🧠 Future Enhancements

* 🤖 AI-based responses (OpenAI integration)
* 🎨 GUI using Tkinter / PyQt
* 🌐 Full Stack Web Version (React + FastAPI)
* 🧠 Conversation memory
* 🎙️ Wake word detection ("Alexa")

---

## 🐛 Known Issues

* pyttsx3 may not work properly on some systems (audio driver issue)
* Requires internet for speech recognition and YouTube playback

---

## ⭐ Contribute

Feel free to fork this repo and improve the project!


