from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings

documents = [
"Machine learning is a subset of artificial intelligence",
"Deep learning uses neural networks with multiple layers",
"Python is a programming language popular for data science",
"India won the cricket world cup in 2011",
"AI models can understand and generate human Language",
"I love to watch movies"
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_embed = embedding_model.embed_documents(documents)

print("Number of documents:", len(vector_embed))
print("Dimensions:", len(vector_embed[0]))