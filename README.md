# Voice Recognition Assistant (Python)

This is a Python-based voice assistant capable of:
- Listening to your voice commands
- Speaking responses using text-to-speech
- Answering factual questions via the WolframAlpha API
- Opening common websites (e.g., Google, YouTube, GitHub)
- Sending SMS messages using Twilio API

---

## 🛠 Features

- Speech recognition using Google's API
- Text-to-speech output via `pyttsx3`
- WolframAlpha integration for knowledge-based queries
- Secure SMS sending via Twilio (with `.env` security)
- Website launcher for frequently used platforms

---

## 🔐 Security

This project uses a `.env` file to protect sensitive credentials:


## 📦 Requirements

Install required Python libraries using pip:

```bash
pip install speechrecognition pyttsx3 wolframalpha twilio python-dotenv
