from fastapi import FastAPI
from pydantic import BaseModel
from app import generate_quiz
from edu_tutor_ai_personalized_learning_with_generative_ai_and_lms_integration import model, tokenizer, device

app = FastAPI()

class QuizRequest(BaseModel):
    topic: str
    num_questions: int

@app.post("/generate-quiz/")
def generate_quiz_api(req: QuizRequest):
    questions = generate_quiz(req.topic, "intermediate", model, tokenizer, device)
    return {"questions": questions[:req.num_questions]}
