from fastapi import FastAPI

from app.models.chat import ChatRequest
from app.services.llm_service import LLMService
from app.agents.intent_agent import IntentAgent

app = FastAPI()

llm_service = LLMService()


@app.get("/")
def root():
    return {
        "message": "A2UI Financial Assistant Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):



    intent_agent = IntentAgent(llm_service)

    response = intent_agent.detect_intent(
        request.message
    )

    return {
        "response": response
    }