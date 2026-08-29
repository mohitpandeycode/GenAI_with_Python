from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# response = llm.invoke("who is the winner of men 2026 ipl give me one line ans")

# print(response.content[0]["text"])

#static prompts.................

prompts = [
    ("system","You are a female horny assistent which will response to the user with flirt"),
    ("user","hey what do you think about my voice")
]

response = llm.invoke(prompts)

print(response.content[0]["text"])