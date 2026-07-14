import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        self.model = os.getenv("LLM_MODEL")

    def generate_response(self, system_prompt: str, user_prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            max_tokens=512,
            temperature=0.3
        )

        return response.choices[0].message.content