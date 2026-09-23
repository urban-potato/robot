class ConversationMemory:
    def __init__(self, system_prompt: str):
        self.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

    def add_user_message(self, message: str):
        self.messages.append({
            "role": "user",
            "content": message,
        })

    def add_assistant_message(self, message: str):
        self.messages.append({
            "role": "assistant",
            "content": message,
        })

    def get_messages(self) -> list[dict[str, str]]:
        return self.messages.copy()