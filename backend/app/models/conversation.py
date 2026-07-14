from pydantic import BaseModel


class ConversationMessage(BaseModel):

    role: str

    content: str