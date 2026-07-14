from pydantic import BaseModel
from typing import Any
from app.models.intent import IntentResponse


class AssistantResponse(BaseModel):

    intent: IntentResponse

    research_plan: str
    ui: dict[str, Any]