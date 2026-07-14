from app.models.intent import IntentResponse
from app.services.llm_service import LLMService
from app.prompts.research_prompt import SYSTEM_PROMPT

class ResearchAgent:

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def plan_research(
        self,
        conversation_history: str,
        user_message: str,
        intent: IntentResponse
    ) -> str:

        user_prompt = f"""
        Conversation History:
        {conversation_history}

        Current User Message:
        {user_message}

        Intent:
        {intent.intent}

        Create the research plan.

        Return only plain text.
        """

        research_plan = self.llm_service.generate_response(
            SYSTEM_PROMPT,
            user_prompt
        )

        return research_plan