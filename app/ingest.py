from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings

# Load and split PDF
loader = PyPDFLoader("docs/sample.pdf")
documents = loader.load_and_split()

# Embed with Hugging Face MiniLM model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in FAISS
db = FAISS.from_documents(documents, embeddings)
db.save_local("vectorstore")

print("✅ Vectorstore created and saved.")
