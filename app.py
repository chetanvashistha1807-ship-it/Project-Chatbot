import os
import streamlit as st
from langchain_core.messages import HumanMessage
from main import create_chatbot

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
)

# -------------------------------
# CSS
# -------------------------------

st.markdown(
    """
<style>

.block-container{
    padding-top:2rem;
    max-width:900px;
}

h1{
    text-align:center;
}

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------
# Initialize Agent
# -------------------------------

if "agent" not in st.session_state:
    st.session_state.agent = create_chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:
    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.subheader("Available Tools")

    st.write("🧮 Calculator")
    st.write("🌤 Current Weather")
    st.write("📈 Weather History")
    st.write("💱 Currency Converter")
    st.write("🌍 Translator")
    st.write("😀Wikipedia")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# Main Page
# -------------------------------

st.title("🤖 AI Assistant")
st.caption("Powered by LangChain + OpenRouter")
st.caption("Developed by **Chetan Vashistha**")

if len(st.session_state.messages) == 0:
    st.info(
        """
### 👋 Welcome!

Try asking:

- What's the weather in Jaipur?
- Convert 100 USD to INR
- Translate "Good Morning" to French
- Show me the weather history of Jaipur
- Calculate 123 + 456
"""
    )

# -------------------------------
# Display Previous Messages
# -------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# Chat Input
# -------------------------------

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ""

            for chunk in st.session_state.agent.stream(
                {"messages": [HumanMessage(content=prompt)]}
            ):
                if "model" in chunk:
                    for message in chunk["model"]["messages"]:
                        response += message.content

            st.markdown(response)

            if (
                "weather" in prompt.lower()
                and "history" in prompt.lower()
                and os.path.exists("weather_chart.png")
            ):
                st.image(
                    "weather_chart.png",
                    caption="Weather History",
                    use_container_width=True,
                )

                csv_path = "data/Jaipur_weather.csv"

                if os.path.exists(csv_path):
                    with open(csv_path, "rb") as f:
                        st.download_button(
                            "⬇ Download Weather CSV",
                            data=f,
                            file_name="Jaipur_weather.csv",
                            mime="text/csv",
                        )

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )