from fastapi import FastAPI

from app.models.chat import ChatRequest
from app.services.llm_service import LLMService
from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent

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
    research_agent = ResearchAgent(llm_service)

    intent = intent_agent.detect_intent(
        request.message
    )

    research_plan = research_agent.plan_research(
        request.message,
        intent
    )

    return {
        "intent": intent,
        "research_plan": research_plan
    }