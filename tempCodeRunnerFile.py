from datetime import datetime, timedelta
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import requests

load_dotenv()


@tool
def current_weather(latitude: float, longitude: float) -> str:
    """Get the current weather for given latitude and longitude.

    Use this tool whenever the user asks about:
    - current weather
    - current temperature
    - humidity
    - wind speed
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch weather data."

    data = response.json()
    current = data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]

    return (
        f"Current Weather\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n"
        f"Temperature: {temperature}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} km/h"
    )


@tool
def translator(text: str, langpair: str) -> str:
    """Use this for translating.
         
         Translate text from one language to another.

         Use this tool whenever the user asks to:
         - translate text
         - convert one language to another
         - translate a sentence """
    
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair={langpair}"

    response = requests.get(url)
    print("The tool has been called")

    if response.status_code != 200:
        return "Unable to translate."
    
    data = response.json()
    return data.get("responseData", {}).get("translatedText", "Unable to translate.")


@tool
def weather_history(latitude: float, longitude: float) -> str:
    """Get weather for the last 7 days for given latitude and longitude.

    Save a CSV and graph.
    Return the weather table.
    """
    # Calculate dates
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    # Format dates for API (YYYY-MM-DD)
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    # Get weather for past week
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch weather history."

    data = response.json()

    # Extract the daily data
    daily_data = data["daily"]

    # Create a DataFrame
    df = pd.DataFrame(
        {
            "date": daily_data["time"],
            "max_temp": daily_data["temperature_2m_max"],
            "min_temp": daily_data["temperature_2m_min"],
        }
    )

    # Convert date strings to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
    plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather History - Past 7 Days")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("weather_chart.png")
    plt.close()

    if not os.path.exists("data"):
        os.makedirs("data")

    df.to_csv("data/Jaipur_weather.csv", index=False)

    return (
        "Weather report generated successfully.\n\n"
        f"{df.to_string(index=False)}\n\n"
        "CSV saved as data/Jaipur_weather.csv\n"
        "Graph saved as weather_chart.png"
    )


@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with two numbers.

    This tool can add two numbers together.
    """
    print("The tool has been called")
    return f"The sum of {a} and {b} is {a + b}"


def main():
    model = ChatOpenAI(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        temperature=0,
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    tools = [calculator, current_weather, weather_history, translator]

    agent_executor = create_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit")
    print("You can ask me to perform calculations or chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant:")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "model" in chunk:
                for message in chunk["model"]["messages"]:
                    print(message.content, end="")

        print()


if __name__ == "__main__":
    main()