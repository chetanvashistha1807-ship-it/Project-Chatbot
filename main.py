import os
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool

load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """
    Useful for performing basic arithmetic calculations with two numbers.

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

    tools = [calculator]

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