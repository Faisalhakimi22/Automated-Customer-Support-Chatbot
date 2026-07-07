# AI Customer Support Chatbot - Portfolio Project Information

## 🎯 Project Overview for Job Applications

Hybrid AI chatbot combining Rasa dialogue management with LLaMA LLM for intelligent customer support.

---

## Elevator Pitch (30 seconds)

"I built an AI-powered customer support chatbot using Rasa 3 for dialogue management and LLaMA for generative responses. The system uses LangChain for Retrieval Augmented Generation (RAG) with ChromaDB, FastAPI for the LLM microservice, and Streamlit for the UI. This demonstrates expertise in conversational AI, LLM integration, microservices architecture, and RAG implementation."

---

## 💼 Business Value

**Problem Solved:**
- Manual customer support is expensive and slow
- Rule-based chatbots lack flexibility
- Need for 24/7 automated support

**Solution Provided:**
- Hybrid system (rules + generative AI)
- Fast local LLM inference (Llama.cpp)
- Document-grounded answers (RAG)
- Scalable microservices architecture

---

## 🛠️ Technical Skills Demonstrated

### **AI/ML & NLP**
- Large Language Models (LLaMA)
- Retrieval Augmented Generation (RAG)
- Conversational AI (Rasa 3)
- Intent classification & entity extraction
- Vector databases (ChromaDB)
- Semantic search

### **Backend Development**
- FastAPI microservice
- Rasa dialogue management
- Custom actions and integrations
- RESTful API design
- Async/await patterns

### **LLM Integration**
- Llama.cpp local inference
- LangChain framework
- Prompt engineering
- Context window management
- Token optimization

### **RAG Pipeline**
- Document ingestion (PDF, DOCX, text)
- Text chunking and embedding
- Vector store (ChromaDB)
- Similarity search
- Context retrieval

### **Frontend**
- Streamlit chat interface
- Real-time messaging
- Session state management
- Responsive design

### **Architecture**
- Microservices pattern
- API-first design
- Separation of concerns
- Scalable deployment

---

## 📊 Project Metrics

- **Components**: 3 microservices (Rasa, FastAPI, Streamlit)
- **LLM**: Local LLaMA model (Q8_0.gguf)
- **Framework**: Rasa 3.6, LangChain, FastAPI
- **RAG**: ChromaDB vector store
- **Architecture**: Hybrid (rules + generative)

---

## 🎨 Design Decisions

### **Why Rasa 3?**
- **Dialogue Management**: Structured conversation flow
- **Intent Classification**: Pre-trained NLP models
- **Extensible**: Custom actions for LLM integration
- **Production-Ready**: Battle-tested framework

### **Why Local LLaMA (Llama.cpp)?**
- **Privacy**: No data sent to external APIs
- **Cost**: Zero inference costs
- **Speed**: Fast local inference
- **Control**: Full model customization

### **Why LangChain + RAG?**
- **Accuracy**: Ground responses in documents
- **Relevance**: Only retrieve pertinent context
- **Scalability**: Easy to add more documents
- **Framework**: Established RAG patterns

### **Why FastAPI?**
- **Performance**: Async/await for high concurrency
- **Type Safety**: Pydantic validation
- **Documentation**: Auto-generated API docs
- **Modern**: Python 3.8+ async features

---

## 🚀 Challenges Overcome

### **Challenge 1: Hybrid Architecture**
**Problem**: Combine rule-based and generative AI

**Solution**:
- Rasa handles structured intents
- Custom action calls LLM API for open-ended queries
- Seamless handoff between systems

### **Challenge 2: RAG Implementation**
**Problem**: Provide accurate, document-grounded answers

**Solution**:
- LangChain document loaders
- ChromaDB for vector storage
- Similarity search for context retrieval
- Prompt engineering to use retrieved context

### **Challenge 3: Local LLM Performance**
**Problem**: Fast inference on consumer hardware

**Solution**:
- Llama.cpp quantized models (Q8_0)
- Efficient memory management
- Batch processing optimization

---

## 💡 What I Learned

### **Technical**
- Rasa framework and dialogue management
- LLM integration patterns
- RAG architecture and implementation
- Vector databases and embeddings
- FastAPI async programming

### **AI/ML**
- Prompt engineering techniques
- Context window management
- Hybrid AI system design
- Model quantization benefits

---

## 🗣️ Interview Talking Points

### **About the Architecture:**
"I built a hybrid chatbot combining Rasa for structured dialogue with LLaMA for generative responses. Rasa handles intent classification and conversation flow, then calls a FastAPI microservice running Llama.cpp for open-ended questions. The LLM uses RAG with ChromaDB to retrieve relevant context from documents before generating answers."

### **About RAG:**
"The RAG pipeline uses LangChain to load documents, chunk them, create embeddings, and store in ChromaDB. When a query comes in, we do semantic search to find relevant chunks, then inject them into the LLM prompt. This grounds the responses in actual documentation rather than relying on the model's training data."

### **About Microservices:**
"I separated concerns into three services: Rasa for dialogue, FastAPI for LLM inference, and Streamlit for UI. This allows independent scaling and deployment. The FastAPI service can handle multiple concurrent requests with async/await, and the LLM runs locally for privacy and cost savings."

---

## 📝 CV/Resume Entry

**Detailed:**
```
AI Customer Support Chatbot | Rasa, LangChain, LLaMA, FastAPI
• Built hybrid chatbot combining Rasa 3 dialogue management with LLaMA LLM 
  for generative responses using LangChain RAG (Retrieval Augmented Generation)
• Implemented FastAPI microservice for LLM inference with Llama.cpp, ChromaDB 
  vector store, and document retrieval pipeline
• Developed Streamlit chat interface with real-time conversation handling
• Deployed microservices architecture with async API calls and scalable design
```

**Compact:**
```
AI Chatbot | Rasa, LLaMA, LangChain, FastAPI
• Hybrid chatbot with Rasa dialogue + LLaMA generative AI + RAG
• FastAPI LLM microservice, ChromaDB vector store, Streamlit UI
```

---

## 🔗 Related Skills

- Conversational AI & chatbots
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Vector databases
- Microservices architecture
- API development
- Python async programming

---

**Last Updated**: January 2025
**Project Status**: Functional, deployable
**Type**: AI/ML Project
