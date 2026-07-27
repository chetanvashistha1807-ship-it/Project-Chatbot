# 🤖 AI Assistant

An AI-powered chatbot built using **LangChain**, **OpenRouter**, and **Streamlit** that can intelligently use tools to answer user queries instead of relying only on the language model.

Built by **Chetan Vashistha**

---

## ✨ Features

- 💬 Conversational AI Chatbot
- 🧮 Calculator Tool
- 🌤 Current Weather Information
- 📈 7-Day Weather History
- 📊 Automatic Weather Graph Generation
- 📄 Export Weather Data as CSV
- 💱 Currency Converter
- 🌍 Language Translator
- 📚 Wikipedia Search
- 🖥️ Clean Streamlit Web Interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- OpenRouter
- Streamlit
- Pandas
- Matplotlib
- Requests
- Wikipedia API
- Open-Meteo API
- Frankfurter Currency API
- MyMemory Translation API

---

## 📂 Project Structure

```
Project-Chatbot/
│
├── app.py                 # Streamlit UI
├── main.py                # Chatbot logic & tools
├── data/
│   └── Jaipur_weather.csv
├── weather_chart.png
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Project-Chatbot.git
```

Move into the project

```bash
cd Project-Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Launch the Streamlit interface

```bash
streamlit run app.py
```

---

## 💡 Example Prompts

```
What's the weather in Jaipur?

Convert 250 USD to INR.

Translate "Good Morning" to French.

Show me the weather history for Jaipur.

Calculate 345 + 678.

Tell me about Artificial Intelligence from Wikipedia.
```

---

## 📷 Weather History

The weather history tool:

- Fetches the previous 7 days' weather
- Creates a temperature graph
- Saves the data as CSV
- Displays the chart directly inside the Streamlit interface

---

## 🔧 APIs Used

- OpenRouter
- Open-Meteo
- Frankfurter Exchange Rates
- MyMemory Translation
- Wikipedia

---

## Future Improvements

- 🔍 Web Search Tool
- 🧠 Conversation Memory
- 📍 Location Detection
- 🎤 Voice Input
- 🔊 Text-to-Speech
- 📂 File Upload & Analysis
- 📄 PDF Question Answering
- 🖼️ Image Understanding
- 🌐 Multi-Agent Support
- ☁️ Cloud Deployment

---

## Author

**Chetan Vashistha**

If you found this project interesting, feel free to star the repository.