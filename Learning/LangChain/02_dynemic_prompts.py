from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)
output = StrOutputParser()

#self chaining function to use on response

def uppercaseOutput(response):
    return response.upper()

#Dynemic prompts / chaining.................

prompts = ChatPromptTemplate.from_messages([
    {"role":"system", "content":"you are a translater tool which translate the user query to the {language} language"},
    {"role":"user", "content":"{input}"}
])

chain = prompts | llm | output | uppercaseOutput  #chaining the runnable outputs

response = chain.invoke({"language": "Hinglish","input":"I love Anjali Mehta"})

print(response)