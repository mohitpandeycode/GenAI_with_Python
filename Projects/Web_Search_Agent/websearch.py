from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-20b")

# tavily search tool
search_tool = TavilySearch(
max_results=1,
topic="general",
)

# web search agent
@tool("web_search", description="Performs web searches to search real time update data for user query")
def web_search(query:str) -> str:
    """this tool can able to perform web searches for the user qyery that can help to fetch real time update data

    Args:
        query (str): user query or question asked by user

    Returns:
        str: best and to the point search result for user query no extra content if not asked
    """
    result = search_tool.invoke(query)
    return str(result)


agent = create_agent(
    model = llm,
    tools=[web_search],
    system_prompt="You are a best search agent Use web_search when current information is required. Give concise answers when the user asks for a short answer."
)

memory = []

while True:
    query = input("User:" )
    memory.append({"role":"user","content":query})
    
    res = agent.invoke({"messages":memory})
    result = res["messages"][-1].content
    memory.append({"role":"ai","content":result})

    print("AI:" ,result)