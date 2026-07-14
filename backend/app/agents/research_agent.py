from app.models.intent import IntentResponse
from app.services.llm_service import LLMService


class ResearchAgent:

    SYSTEM_PROMPT = """
You are a Financial Research Planning Agent.

Your job is NOT to answer the user's question.

Your job is to create a research plan for another AI agent.

The Intent Agent has already determined whether follow-up questions are needed.

Do NOT ask the user any questions.

Assume the user's request is complete.

Return only the information that should be collected.

Return only plain text.

Examples:

User Query:
Compare Apple and Microsoft

Output:
Collect:
- Company overview
- Market capitalization
- Revenue
- Net profit
- P/E ratio
- Earnings growth
- Recent financial performance

User Query:
Explain P/E Ratio

Output:
Collect:
- Definition
- Formula
- Interpretation
- Advantages
- Limitations
- Practical example
"""

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def plan_research(
        self,
        user_message: str,
        intent: IntentResponse
    ) -> str:

        user_prompt = f"""
Intent:
{intent.intent}

User Query:
{user_message}
"""

        research_plan = self.llm_service.generate_response(
            self.SYSTEM_PROMPT,
            user_prompt
        )

        return research_plan