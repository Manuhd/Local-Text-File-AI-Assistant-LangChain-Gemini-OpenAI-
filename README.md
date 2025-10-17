# 🧠 Local AI File Assistant (LangChain + Gemini)

A simple Python project that uses LangChain and Google Gemini AI to answer questions from your local text files.
This is a great starting point for learning how to build AI-powered assistants that understand and respond using your own data.

## 🚀 Features

Uses LangChain with Gemini AI (Google Generative AI)

Reads and understands content from a local .txt file

Answers user questions using context-aware reasoning

Simple CLI-based interaction (no frontend required)

## 🧩 Requirements

Make sure you have Python 3.10+ installed.

Install dependencies:

pip install langchain langchain-community langchain-google-genai google-generativeai python-dotenv

## 📁 Project Structure
`ai-file-assistant/
├── main.py
├── data.txt
└── .env`

## ⚙️ Setup
### 1. Create a .env file

Add your Gemini API key:

GOOGLE_API_KEY=your_gemini_api_key_here

### 2. Add data to data.txt

### Example:

Product: Camera X100
Price: 45000
Features: 4K video, 24MP, WiFi, Bluetooth

Product: Sony Tripod
Price: 5000
Features: Adjustable height, lightweight aluminum, 1.5kg max load

## 🧠 Run the Assistant
### `python main.py`


## Example:

## 👤 You: Which product has WiFi?
## 🤖 AI: The Camera X100 supports WiFi.

## 🧩 How It Works

The text file (data.txt) acts as the context for the AI.

The query you type is passed to LangChain.

LangChain sends both the file content and your query to the Gemini AI model.

Gemini reads the context and returns an accurate answer.

## 💡 Next Steps (For Advanced Users)

Add multiple files and use a document loader.

Add memory so the assistant remembers past chats.

Replace the text file with a WordPress API or database.

Build a React frontend for a chat-like interface.

## 🛠️ Tech Stack

Python 3.10+

LangChain

Google Generative AI (Gemini)

dotenv (for environment variables)

👨‍💻 Author

Manu HD
Full Stack Developer | WordPress & AI Integrations
💼 LinkedIn
 • 🌐 Portfolio

