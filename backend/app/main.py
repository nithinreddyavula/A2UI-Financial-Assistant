from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.chat import ChatRequest
from app.services.llm_service import LLMService
from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent
from app.services.financial_assistant_service import FinancialAssistantService
from fastapi.responses import StreamingResponse
import json
from app.utils.fallback_ui import get_fallback_ui

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
        request.message,
        request.formData
    )

    return response
@app.post("/conversation/clear")
def clear_conversation():

    assistant_service.conversation_manager.clear()

    return {
        "message": "Conversation cleared."
    }

@app.post("/chat/stream")
def stream_chat(request: ChatRequest):

    def event_stream():

        yield "data: Detecting Intent...\n\n"

        intent = assistant_service.intent_agent.detect_intent(
            "",
            request.message
        )

        yield "data: Planning Research...\n\n"

        research_plan = assistant_service.research_agent.plan_research(
            "",
            request.message,
            intent
        )

        yield "data: Generating UI...\n\n"

        ui = assistant_service.ui_generator_agent.generate_ui(
            "",
            request.message,
            intent,
            research_plan,
            False
        )

        yield "data: Validating UI...\n\n"

        validation = assistant_service.validator_agent.validate(ui)

        if not validation.valid:
            ui = get_fallback_ui()

        yield "data: Done\n\n"

        yield f"data: {json.dumps(ui)}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream"
    )