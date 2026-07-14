from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent
from app.agents.ui_generator_agent import UIGeneratorAgent
from app.models.assistant import AssistantResponse
from app.services.llm_service import LLMService


class FinancialAssistantService:

    def __init__(self, llm_service: LLMService):

        self.intent_agent = IntentAgent(llm_service)

        self.research_agent = ResearchAgent(llm_service)

        self.ui_generator_agent = UIGeneratorAgent(llm_service)

    def process(
        self,
        user_message: str
    ) -> AssistantResponse:

        intent = self.intent_agent.detect_intent(
            user_message
        )

        research_plan = self.research_agent.plan_research(
            user_message,
            intent
        )

        ui = self.ui_generator_agent.generate_ui(
            user_message,
            intent,
            research_plan
        )

        return AssistantResponse(
            intent=intent,
            research_plan=research_plan,
            ui=ui
        )