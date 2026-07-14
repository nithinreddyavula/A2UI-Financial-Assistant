import json

from app.models.intent import IntentResponse
from app.services.llm_service import LLMService
from app.prompts.intent_prompt import SYSTEM_PROMPT


class IntentAgent:

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def detect_intent(
        self,
        conversation_history: str,
        user_message: str
    ) -> IntentResponse:

        user_prompt = f"""
        Conversation History

        {conversation_history}

        Current User Message

        {user_message}
        """

        response = self.llm_service.generate_response(
            SYSTEM_PROMPT,
            user_prompt
        )



        intent_json = json.loads(response)

        return IntentResponse(**intent_json)