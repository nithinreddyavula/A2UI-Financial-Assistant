from fastapi import FastAPI

from app.models.chat import ChatRequest
from app.services.llm_service import LLMService

app = FastAPI()

llm_service = LLMService()


@app.get("/")
def root():
    return {
        "message": "A2UI Financial Assistant Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = llm_service.generate_response(
        request.message
    )

    return {
        "response": response
    }