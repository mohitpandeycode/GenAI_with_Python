from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader

# Loading text Data 
text_loader = TextLoader("./data/sample.txt", encoding="utf-8")
text_data = text_loader.load()

# print(text_data[0].page_content)

# chunking text data 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=40)
texts = text_splitter.split_documents(text_data)

# # print text chunk data 
# for i in texts:
#     print ([i.page_content],"\n")


# loading pdf data 
pdf_loader = PyPDFLoader("./data/Lab Assignment 8.pdf")
pdf_data = pdf_loader.load()

# for data in pdf_data:
#     print(data.page_content)

# chunking pdf data 
pdf_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = pdf_splitter.split_documents(pdf_data)

print(len(chunks))

for data in chunks:
    print([data.page_content],"\n\n")