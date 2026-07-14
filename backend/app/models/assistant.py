from pydantic import BaseModel

from app.models.intent import IntentResponse


class AssistantResponse(BaseModel):

    intent: IntentResponse

    research_plan: str