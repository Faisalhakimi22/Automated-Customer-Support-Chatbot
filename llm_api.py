from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os

from langchain_community.llms import LlamaCpp
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PDFPlumberLoader, UnstructuredMarkdownLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import LlamaCppEmbeddings
from langchain.chains import ConversationalRetrievalChain

# Path to your local Unsloth GGUF model (e.g., D:\\unsloth.Q8_0.gguf)
GGUF_MODEL_PATH = os.getenv("GGUF_MODEL_PATH", r"D:\\Automated-Customer-Support-Chatbot\\models\\unsloth.Q8_0.gguf")

# Llama.cpp runtime configuration (override via env vars if desired)
LLM_CTX = int(os.getenv("LLM_CTX", "4096"))          # Context window
N_GPU_LAYERS = int(os.getenv("N_GPU_LAYERS", "0"))   # GPU layers to offload (0 = CPU only)

DOCS_PATH = os.getenv("DOCS_PATH", "docs")
CHROMA_PATH = os.getenv("CHROMA_PATH", "chroma_db")

app = FastAPI(title="Advanced LLM Chatbot API with LangChain RAG")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: List[Message] = []
    model: str = "mistral" # This will be ignored by LlamaCpp
    use_rag: bool = True

def build_vectorstore():
    loaders = [
        DirectoryLoader(DOCS_PATH, glob="**/*.txt", loader_cls=TextLoader),
        DirectoryLoader(DOCS_PATH, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader),
        DirectoryLoader(DOCS_PATH, glob="**/*.pdf", loader_cls=PDFPlumberLoader),
    ]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    embeddings = LlamaCppEmbeddings(model_path=GGUF_MODEL_PATH, n_ctx=LLM_CTX)
    vectordb = Chroma.from_documents(splits, embeddings, persist_directory=CHROMA_PATH)
    vectordb.persist()
    return vectordb

if not os.path.exists(CHROMA_PATH):
    os.makedirs(CHROMA_PATH, exist_ok=True)
    vectordb = build_vectorstore()
else:
    embeddings = LlamaCppEmbeddings(model_path=GGUF_MODEL_PATH, n_ctx=LLM_CTX)
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

llm = LlamaCpp(
    model_path=GGUF_MODEL_PATH,
    n_ctx=LLM_CTX,
    n_gpu_layers=N_GPU_LAYERS,
)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True
)

@app.post("/chat")
def chat(req: ChatRequest):
    if req.use_rag:
        chat_history = [(msg.role, msg.content) for msg in req.history]
        result = qa_chain({"question": req.message, "chat_history": chat_history})
        answer = result["answer"]
        sources = [doc.metadata.get("source", "") for doc in result["source_documents"]]
        return {
            "response": f"{answer}\n\nSources: {', '.join(sources)}",
            "sources": sources
        }
    else:
        response = llm.invoke(req.message)
        return {"response": response}

@app.get("/")
def root():
    return {"status": "ok", "message": "Advanced LLM API with LangChain RAG is running. Use POST /chat."} 