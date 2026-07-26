# 🤖 AI Chatbot with LangChain & OpenRouter

A simple AI chatbot built using **Python**, **LangChain**, and **OpenRouter**. This project demonstrates how to create an AI agent capable of engaging in conversations using Large Language Models (LLMs).

## 🚀 Features

- Interactive command-line chatbot
- Built using LangChain's Agent framework
- Uses OpenRouter as the LLM provider
- Secure API key management with `.env`
- Easily extensible with custom tools
- Clean and beginner-friendly project structure

## 🛠️ Tech Stack

- Python 3.12
- LangChain
- LangChain OpenAI
- OpenRouter API
- Python Dotenv

## 📂 Project Structure

```
Project Chatbot/
│── .venv/
│── .env
│── main.py
│── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chetanvashistha1807-ship-it/project-chatbot.git
cd project-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root and add your OpenRouter API key.

```env
OPENROUTER_API_KEY=your_api_key_here
```

## ▶️ Run the Project

```bash
python main.py
```

Example:

```
Welcome! I'm your AI assistant. Type 'quit' to exit

You: Hello!

Assistant:
Hi there! How can I help you today?
```

## 📦 Dependencies

- langchain
- langchain-core
- langchain-openai
- python-dotenv

## 📈 Future Improvements

- Add custom tools (calculator, weather, etc.)
- Conversation memory
- Stream responses token-by-token
- Web search integration
- GUI using Streamlit or Gradio
- Voice input and output

## 📚 What I Learned

- Working with LangChain Agents
- Integrating OpenRouter with LangChain
- Managing API keys using environment variables
- Building conversational AI applications in Python
- Handling streaming responses from LLMs

## 📄 License

This project is open source and available under the MIT License.
