from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

class Movies(BaseModel):
    name:str = Field(description="Name of the movie")
    year:int = Field(description="year of the movie release")
    main_cast:list = Field(description="main actor and actoress name only")
    
class AllMovies(BaseModel):
    movies : List[Movies]
    
# movieLLM = llm.with_structured_output(Movies)
movieLLM = llm.with_structured_output(AllMovies)

res = movieLLM.invoke("latest 5 adult A rated movie")

print(res.model_dump())
# print(res.name)
# print(res.year)
# print(res.main_cast)
