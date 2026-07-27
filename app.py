import streamlit as st
from langchain_core.messages import HumanMessage

from main import create_chatbot

# Create the chatbot
agent = create_chatbot()

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Assistant")
st.write("Ask me anything!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate response
    answer = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:
            for chunk in agent.stream(
                {
                    "messages": [
                        HumanMessage(content=prompt)
                    ]
                }
            ):

                if "model" in chunk:
                    for message in chunk["model"]["messages"]:
                        answer += message.content
                        placeholder.markdown(answer + "▌")

            placeholder.markdown(answer)

        except Exception as e:
            answer = f"❌ Error:\n\n{e}"
            placeholder.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )