from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# tool for create introduction

@tool
def create_intro(name:str) -> str:
    """ this function can take user name and then give the introduction using the result of this fonction

    Args:
        name (str): this takes user name from the input

    Returns:
        str: it returns the introduction of the user
    """
    result = f"Hi My name is {name.title()}. Whatsup everyone"
    return result


agent = create_agent(
    model = llm,
    tools=[create_intro],
    system_prompt="Your are a introduction maker tool that uses the mentioned tools to make the introduction of the user"
)


res = agent.invoke({"messages":[{"role":"user","content":"mera nam mohit pandey hai"}]})
# print(res["messages"][-1].content[0]["text"])
print(res["messages"][-1].text)