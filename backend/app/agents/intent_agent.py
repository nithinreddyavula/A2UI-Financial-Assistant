import json

from app.models.intent import IntentResponse
from app.services.llm_service import LLMService


class IntentAgent:

    SYSTEM_PROMPT = """
You are an Intent Classification Agent.

Your job is to identify only the user's intent.

Return ONLY valid JSON.

Available intents:

GREETING
COMPARE
ALLOCATE
REBALANCE
QUESTION

If more information is required,
set needs_follow_up to true.

Examples:

User:
Hello

Response:
{
    "intent":"GREETING",
    "needs_follow_up":false
}

User:
Compare RELIANCE and TCS

Response:
{
    "intent":"COMPARE",
    "needs_follow_up":false
}

User:
I want to invest ₹50,000

Response:
{
    "intent":"ALLOCATE",
    "needs_follow_up":true
}
"""

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def detect_intent(self, user_message: str) -> IntentResponse:

        response = self.llm_service.generate_response(
            self.SYSTEM_PROMPT,
            user_message
        )


        intent_json = json.loads(response)

        return IntentResponse(**intent_json)