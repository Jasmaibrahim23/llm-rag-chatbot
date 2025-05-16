from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load Ollama (e.g., mistral)
llm = Ollama(model="mistral")

# Load FAISS index + embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#db = FAISS.load_local("vectorstore", embeddings)
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)


# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

# Function to answer questions
def ask_question(query):
    response = qa_chain.invoke({"query": query})

    return response
