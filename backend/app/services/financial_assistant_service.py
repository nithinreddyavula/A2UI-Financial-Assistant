from app.agents.intent_agent import IntentAgent
from app.agents.research_agent import ResearchAgent
from app.models.assistant import AssistantResponse
from app.services.llm_service import LLMService


class FinancialAssistantService:

    def __init__(self, llm_service: LLMService):

        self.intent_agent = IntentAgent(llm_service)

        self.research_agent = ResearchAgent(llm_service)

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

        return AssistantResponse(
            intent=intent,
            research_plan=research_plan
        )