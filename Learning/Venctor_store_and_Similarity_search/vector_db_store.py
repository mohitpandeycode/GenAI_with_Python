from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

documents = [
"Machine learning is a subset of artificial intelligence",
"Deep learning uses neural networks with multiple layers",
"Python is a programming language popular for data science",
"India won the cricket world cup in 2011",
"AI models can understand and generate human Language",
"I love to watch movies"
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embedding_model,
    persist_directory="./chroma_langchain_db",  # Where to save data locally
)

query = " in 2011"

result = vector_store.similarity_search(query, k=2)

for i in result:
    print(i.page_content)




