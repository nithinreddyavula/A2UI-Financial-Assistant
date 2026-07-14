from app.models.conversation import ConversationMessage


class ConversationManager:

    def __init__(self):

        self.history: list[ConversationMessage] = []

    def add_user_message(
        self,
        content: str
    ):

        self.history.append(

            ConversationMessage(
                role="user",
                content=content
            )

        )

    def add_assistant_message(
        self,
        content: str
    ):

        self.history.append(

            ConversationMessage(
                role="assistant",
                content=content
            )

        )

    def get_history(self):

        return self.history

    def get_history_as_text(self) -> str:

        conversation = ""

        for message in self.history:

            conversation += (
                f"{message.role}: "
                f"{message.content}\n"
            )

        return conversation.strip()

    def clear(self):

        self.history.clear()