import json

from app.models.intent import IntentResponse
from app.services.llm_service import LLMService
from app.prompts.intent_prompt import SYSTEM_PROMPT


class IntentAgent:

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def detect_intent(self, user_message: str) -> IntentResponse:

        response = self.llm_service.generate_response(
            SYSTEM_PROMPT,
            user_message
        )



        intent_json = json.loads(response)

        return IntentResponse(**intent_json)