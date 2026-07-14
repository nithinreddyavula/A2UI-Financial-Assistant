from fastapi import FastAPI

from app.models.chat import ChatRequest
from app.services.llm_service import LLMService
from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent
from app.services.financial_assistant_service import FinancialAssistantService

app = FastAPI()
llm_service = LLMService()

assistant_service = FinancialAssistantService(
    llm_service
)


@app.get("/")
def root():
    return {
        "message": "A2UI Financial Assistant Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = assistant_service.process(
        request.message
    )

    return response