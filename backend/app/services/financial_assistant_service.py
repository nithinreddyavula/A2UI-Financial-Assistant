from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent
from app.agents.ui_generator_agent import UIGeneratorAgent
from app.agents.validator_agent import ValidatorAgent

from app.models.assistant import AssistantResponse

from app.services.llm_service import LLMService
from app.services.conversation_manager import ConversationManager

from app.utils.fallback_ui import get_fallback_ui


class FinancialAssistantService:

    def __init__(self, llm_service: LLMService):

        self.intent_agent = IntentAgent(llm_service)

        self.research_agent = ResearchAgent(llm_service)

        self.ui_generator_agent = UIGeneratorAgent(llm_service)

        self.validator_agent = ValidatorAgent()

        self.conversation_manager = ConversationManager()

    def _generate_valid_ui(
        self,
        conversation_history: str,
        user_message: str,
        intent,
        research_plan: str,
        form_submitted: bool
    ) -> dict:

        ui = self.ui_generator_agent.generate_ui(
            conversation_history,
            user_message,
            intent,
            research_plan,
            form_submitted
        )

        validation = self.validator_agent.validate(ui)

        print("\nValidation Result")
        print(validation)

        if not validation.valid:

            print("\nRetrying UI Generation...")

            ui = self.ui_generator_agent.generate_ui(
                conversation_history,
                user_message,
                intent,
                research_plan,
                form_submitted
            )

            validation = self.validator_agent.validate(ui)

        if not validation.valid:

            print("\nRetry Failed")
            print(validation.reason)

            ui = get_fallback_ui()

        return ui

    def process(
        self,
        user_message: str,
        form_data: dict | None = None
    ) -> AssistantResponse:

        self.conversation_manager.add_user_message(
            user_message
        )

        conversation_history = (
            self.conversation_manager
            .get_history_as_text()
        )

        intent = self.intent_agent.detect_intent(
            conversation_history,
            user_message
        )

        if form_data:

            research_plan = f"""
User Preferences

Amount: {form_data.get("amount")}

Risk: {form_data.get("risk")}

Investment Horizon: {form_data.get("horizon")}

Generate a recommendation.
"""

            ui = self.ui_generator_agent.generate_ui(
                conversation_history,
                user_message,
                intent,
                research_plan,
                True
            )

            self.conversation_manager.add_assistant_message(
                "Generated investment recommendation."
            )

            return AssistantResponse(
                intent=intent,
                research_plan=research_plan,
                ui=ui
            )

        research_plan = self.research_agent.plan_research(
            conversation_history,
            user_message,
            intent
        )

        ui = self.ui_generator_agent.generate_ui(
            conversation_history,
            user_message,
            intent,
            research_plan,
            False
        )

        self.conversation_manager.add_assistant_message(
            "Generated interface."
        )

        return AssistantResponse(
            intent=intent,
            research_plan=research_plan,
            ui=ui
        )