from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-120b", streaming = True)

question = "explain me genAI"

res = llm.stream(question)

for chunk in res:
    print(chunk.content, end="")
