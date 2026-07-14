from pydantic import BaseModel


class IntentResponse(BaseModel):
    intent: str
    needs_follow_up: bool