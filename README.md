# 🚀 LLM Customer Insights Copilot (RAG + Agentic AI)

A production-style backend system that analyzes customer feedback and enables intelligent querying using **Retrieval-Augmented Generation (RAG)** and **Agentic AI workflows**.

This project demonstrates how to design scalable, modular LLM systems with **vector search, caching, multi-step reasoning, and dynamic orchestration**.

---

## 🧠 Problem Statement

Customer feedback is unstructured and difficult to analyze at scale.

This system:

* Converts feedback into structured insights
* Stores semantic representations (embeddings)
* Enables natural language querying over historical data
* Supports **multi-step investigation using an AI agent**

---

## 🔥 Key Features

* LLM-based feedback analysis (sentiment, topics, priority)
* Vector database (ChromaDB) for semantic search
* RAG pipeline for contextual Q&A (`/ask`)
* Agentic workflow for complex queries (`/agent`)
* Multi-step reasoning (analysis → final answer)
* Caching (embedding + semantic answer cache)
* Clean, reusable architecture (no duplication)

---

## 🏗️ Architecture Overview

```
User
  ↓
FastAPI (API Layer)
  ↓
Orchestration Layer
  ├── RAG Service (/ask)
  └── Agent Service (/agent)
  ↓
Shared Services
  ├── Retrieval Service (Vector DB)
  ├── Filtering Service
  ├── Analysis Service (LLM)
  ├── Intent Service
  ├── Cache Service
  ↓
ChromaDB (Vector Database)
  ↓
LLM Provider (OpenAI)
```

---

## 🔄 Core Workflows

### 🔹 /analyze (Data ingestion)

```
Feedback
→ LLM analysis
→ Structured output
→ Embedding
→ Stored in ChromaDB
```

---

### 🔹 /ask (RAG pipeline)

```
Question
→ Cache check
→ Intent detection
→ Vector search (ChromaDB)
→ Intent-based filtering
→ Intermediate analysis (LLM)
→ Final answer (LLM)
```

---

### 🔹 /agent (Agentic workflow)

```
Question
→ LLM planner (decides steps)
→ Multi-step execution
    retrieve → filter → analyze → summarize
→ Final answer
```

---

## 🎯 When to Use Which Endpoint

* `/ask` → Fast, structured Q&A using RAG
* `/agent` → Complex investigation with multi-step reasoning

---

## 🧠 Key Design Concepts

* Retrieval-Augmented Generation (RAG)
* Agentic AI (planning + tool execution)
* Vector search using embeddings
* Separation of concerns (modular services)
* Multi-step LLM reasoning
* Caching strategies
* Prompt engineering

---

## 🛠️ Tech Stack

* Python
* FastAPI
* OpenAI API
* ChromaDB (Vector Database)
* NumPy
* JSON (for debug storage)

---

## 📦 Project Structure

```
providers/        → LLM & embedding providers
services/
  ├── rag_service.py        → RAG orchestration
  ├── agent_service.py      → Agent orchestration
  ├── retrieval_service.py  → vector search
  ├── filtering_service.py  → filtering logic
  ├── analysis_service.py   → intermediate reasoning
  ├── intent_service.py     → intent detection
  ├── cache_service.py      → caching
repositories/     → vector DB interaction
main.py           → API layer
```

---

## ▶️ How to Run

### 1. Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Add API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_key_here
```

---

### 3. Run Server

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

---

### Ask (RAG)

```json
{
  "question": "What are the main complaints?"
}
```

---

### Agent (Advanced)

```json
{
  "question": "Investigate customer dissatisfaction and suggest next actions"
}
```

---

## 🧠 What Makes This Project Strong

* Goes beyond basic RAG → includes agentic AI
* Implements production-style architecture
* Demonstrates multi-step reasoning
* Uses vector DB instead of file-based search
* Applies real system design principles

---

## 🚀 Future Improvements

* Evaluation framework (LLM output quality)
* Hybrid search (keyword + vector)
* Re-ranking layer
* Redis-based distributed caching
* Monitoring & observability
* UI dashboard

---

## 📌 Note

This is a learning-focused system designed with production patterns.
In real-world systems, additional layers like security, rate limiting, and monitoring would be added.

---

## 👩‍💻 Author

Built as part of LLM system design and AI engineering learning journey.
