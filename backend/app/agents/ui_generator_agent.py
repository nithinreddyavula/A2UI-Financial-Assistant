import json
from app.prompts.ui_prompt import SYSTEM_PROMPT
from app.models.intent import IntentResponse
from app.services.llm_service import LLMService


class UIGeneratorAgent:

    def __init__(self, llm_service: LLMService):

        self.llm_service = llm_service

    def generate_ui(
        self,
        user_message: str,
        intent: IntentResponse,
        research_plan: str,
        form_submitted: bool = False
    ) -> dict:

        user_prompt = f"""
User Query:
{user_message}

Intent:
{intent.intent}

Research Plan:
{research_plan}

Form Submitted:
{"Yes" if form_submitted else "No"}

Design the most appropriate interface.

Return ONLY valid JSON.
"""

        response = self.llm_service.generate_response(
            SYSTEM_PROMPT,
            user_prompt
        )

        ui_json = json.loads(response)

        return ui_json