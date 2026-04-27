from fastapi import FastAPI
from pydantic import BaseModel

from repositories.data_repository import get_all_records
from services.feedback_service import analyze_feedback
from services.rag_service import ask_question


app = FastAPI()


class AnalyzeRequest(BaseModel):
    customer_id: str
    feedback: str


class QuestionRequest(BaseModel):
    question: str


class AnalyzeResponse(BaseModel):
    customer_id: str
    sentiment: str
    topics: list[str]
    priority: str
    recommended_action: str


@app.get("/")
def home():
    return {"message": "LLM API is running"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    try:
        return analyze_feedback(
            customer_id=request.customer_id,
            feedback=request.feedback
        )
    except Exception as e:
        return {"error": str(e)}


@app.get("/results")
def get_results():
    return get_all_records()


@app.post("/ask")
def ask(request: QuestionRequest):
    try:
        answer = ask_question(request.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}