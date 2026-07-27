# 🤖 AI Chatbot with LangChain & OpenRouter

An AI-powered command-line chatbot built using **Python**, **LangChain**, and **OpenRouter**. The chatbot can answer general questions using an LLM while intelligently invoking external tools for weather, currency conversion, translation, calculations, and historical weather analysis.

## ✨ Features

- 🧠 Conversational AI using OpenRouter
- 🌤️ Current weather lookup
- 📊 7-day weather history with graph generation
- 💱 Currency conversion
- 🌍 Language translation
- ➕ Calculator tool
- 📁 Automatically saves weather data as CSV
- 📈 Generates weather history charts

---

## 🛠️ Technologies Used

- Python
- LangChain
- OpenRouter API
- Open-Meteo API
- Frankfurter Currency API
- MyMemory Translation API
- Pandas
- Matplotlib
- Requests
- python-dotenv

---

## 📂 Project Structure

```
Project-Chatbot/
│
├── data/
│   └── Jaipur_weather.csv
│
├── weather_chart.png
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Project-Chatbot.git
cd Project-Chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run the chatbot

```bash
python main.py
```

---

# 🧰 Available Tools

## 🌤️ Current Weather

Get the current weather using latitude and longitude.

Example:

```
What's the weather at latitude 26.91 and longitude 75.78?
```

Returns:

- Temperature
- Humidity
- Wind Speed

---

## 📊 Weather History

Fetches weather data for the previous 7 days.

Features:

- Saves data as CSV
- Generates a temperature graph
- Displays weather table

Generated files:

```
data/Jaipur_weather.csv
weather_chart.png
```

---

## 💱 Currency Converter

Convert between currencies using the Frankfurter API.

Example:

```
Convert 100 USD to INR
```

---

## 🌍 Translator

Translate text between languages using the MyMemory Translation API.

Example:

```
Translate "Good Morning" from English to French
```

---

## ➕

Performs simple arithmetic operations.

Example:

```
Add 25 and 17
```

---

# 📸 Example Conversation

```
You: Convert 100 USD to INR

Assistant:
100 USD = 8763.42 INR
```

```
You: Translate "How are you?" from English to Hindi

Assistant:
आप कैसे हैं?
```

```
You: What's the weather at latitude 26.91 and longitude 75.78?

Assistant:
Current Weather

Temperature: 34°C
Humidity: 61%
Wind Speed: 12 km/h
```

---

# 📦 APIs Used

- OpenRouter
- Open-Meteo
- Frankfurter Currency API
- MyMemory Translation API

---

# 🚀 Future Improvements

- Web Search
- PDF Reader
- CSV Analyzer
- OCR (Image to Text)
- News API
- GitHub Search
- ArXiv Research Search
- Memory Support
- Voice Input & Output
- Streamlit / React Web Interface
- Chat History
- File Upload Support

---

# 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ using Python, LangChain, and OpenRouter.