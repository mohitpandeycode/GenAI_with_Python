from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st

# DB connection and initialize tabels:

db = SQLDatabase.from_uri("sqlite:///C:/Users/mp769/Documents/Web Projects/GenAI_Python/Projects/SQL_task_agent/tasks.db")
db.run("""
       
       CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK (status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       );
       
""")

# LLM model, memory and Sql Tool initialized

llm_model = ChatGroq(model="openai/gpt-oss-20b")
toolkit = SQLDatabaseToolkit(db=db,llm=llm_model)
tool = toolkit.get_tools()
memory = InMemorySaver()


# System Prompt for ai model 
SYSTEM_PROMPT = """

You are a task management assistant that interacts with a SQL database containing a 'tasks'

TASK RULES:
1. Limit SELECT queries to 10 results max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE, confirm with SELECT query
3. If the user requests a list of tasks, present the output in a structured table format to ensure the represented data is clean

CRUD OPERATIONS:
CREATE: INSERT INTO tasks(title, description, status)
READ: SELECT * FROM tasks WHERE ... LIMIT 10
UPDATE: UPDATE tasks SET status =? WHERE id =? OR title =?
DELETE: DELETE FROM tasks WHERE id =? OR title =?

Table schema: id, title, description, status(pending/in_progress/completed), created_at.

"""

# creating agent to connect all of these
st.subheader("🐰 Your ToDo AI")
st.markdown("Your personal AI that help you to manage todo's")

@st.cache_resource
def sql_agent():
    agent = create_agent(
        model=llm_model,
        tools = tool,
        checkpointer= memory,
        system_prompt= SYSTEM_PROMPT
        
    )
    return agent


agent = sql_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])


query = st.chat_input("I remember for you, just tell me...")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role":"user", "content":query})

    with st.chat_message("ai"):
        with st.spinner("Processing..."):
            response = agent.invoke(
                    {"messages":[{"role":"user", "content":query}]},
                    {"configurable":{"thread_id":"1"}}
                )
            result = response["messages"][-1].content
            st.markdown(result)
            st.session_state.messages.append({"role":"ai", "content":result})