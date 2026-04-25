# 🚀 LLM Feedback Analyzer (RAG-based System)

An AI-powered backend system that analyzes customer feedback and enables intelligent querying using **Retrieval-Augmented Generation (RAG)**.

This project demonstrates how to design and build a production-style LLM system with clear architectural separation of concerns.

---

## 🧠 Problem Statement

Customer feedback is unstructured and difficult to analyze at scale.

This system:

* Converts feedback into structured insights
* Stores semantic representations (embeddings)
* Enables natural language querying over historical data

---

## 🔥 Key Features

* ✅ LLM-based feedback analysis (sentiment, topics, priority)
* ✅ Embedding-based semantic search
* ✅ RAG pipeline for contextual Q&A
* ✅ Modular architecture (API, services, providers, retrieval)
* ✅ Pluggable LLM & embedding providers

---

## 🏗️ Architecture

```text
User
 ↓
API Layer (FastAPI)
 ↓
Service Layer (Orchestration)
 ↓
Embedding Layer
 ↓
Retrieval Layer (Similarity Search)
 ↓
LLM Provider
 ↓
Response
```

### Flows

#### `/analyze`

Feedback → LLM → Structured JSON → Embedding → Storage

#### `/ask`

Question → Embedding → Similarity Search → Context → LLM → Answer

---

## 🛠️ Tech Stack

* Python
* FastAPI
* OpenAI API
* NumPy (similarity)
* JSON (storage)

---

## 📦 Project Structure

```text
providers/     → LLM & embedding providers
services/      → orchestration logic
repositories/  → data storage
utils/         → similarity logic
main.py        → API layer
```

---

## ▶️ How to Run

### 1. Setup environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add API key

Create `.env` file:

```env
OPENAI_API_KEY=your_key_here
```

### 3. Run server

```bash
uvicorn main:app --reload
```

Open:
👉 http://127.0.0.1:8000/docs

---

## 🧪 Example Usage

### Analyze feedback

```json
{
  "customer_id": "C101",
  "feedback": "Food was cold and service was slow"
}
```

### Ask questions

```json
{
  "question": "What are the most common complaints?"
}
```

---

## 🧠 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Embeddings & vector similarity search
* Prompt engineering for structured output
* Separation of concerns in LLM systems
* Provider abstraction (LLM & embedding layers)

---

## 🚀 Future Improvements

* Vector database integration (Pinecone / Weaviate)
* Caching layer
* Monitoring & logging
* Guardrails for hallucination control
* UI for feedback analysis

---

## 📌 Note

This is a prototype system. In production, file-based storage would be replaced with a scalable database and vector store.

---

## 👩‍💻 Author

Built as part of LLM system design learning journey.
