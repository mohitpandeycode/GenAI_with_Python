from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a loving, caring, playful girlfriend. "
        "Talk naturally like a real person, not like an AI. "
        "Be cute, supportive, sometimes teasing, and keep the conversation casual and natural."
    ),
    MessagesPlaceholder("history"),
    ("user", "{input}")
])

chain = PROMPT | llm

st.title("Butki ❤️")
st.markdown("my love")

# Store conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Store messages for displaying them in Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
query = st.chat_input("Enter your message")

if query:

    # Show user message
    st.chat_message("user").markdown(query)

    # Send current query + previous history to Gemini
    response = chain.invoke({
        "history": st.session_state.history,
        "input": query
    })

    # Extract response
    answer = response.content[0]["text"]

    # Show AI response
    st.chat_message("assistant").markdown(answer)

    # Save user message to history
    st.session_state.history.append({
        "role": "user",
        "content": query
    })

    # Save AI response to history
    st.session_state.history.append({
        "role": "assistant",
        "content": answer
    })

    # Save messages for Streamlit UI
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })