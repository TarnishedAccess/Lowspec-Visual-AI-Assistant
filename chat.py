import openai
from config import DEFAULTCONTEXT, API_KEY

class ChatManager:
    def __init__(self, model, context=DEFAULTCONTEXT, memory=None, memory_limit=10):
        self.model = model
        self.context = f"CONTEXT: {context}"
        self.memory = memory if memory is not None else []
        self.memory_limit = memory_limit

    def reset_context(self):
        self.context = DEFAULTCONTEXT

    def change_context(self, new_context):
        self.context = f"CONTEXT: {new_context}"

    def wipe_memory(self):
        self.memory.clear()

    def update_memory(self, user, user_message, bot_message):
        self.memory.extend(
            [
                {"role": "user", "content": f"{user}: {user_message}"},
                {"role": "assistant", "content": bot_message},
            ]
        )

        while len(self.memory)>self.memory_limit:
            self.memory.pop(0)

    def get_response(self, user, user_message):
        messages = []
        messages.append({"role": "system", "content": self.context})
        messages.extend(self.memory)
        messages.append({"role": "user", "content": f"{user}: {user_message}"})
        response = openai.ChatCompletion.create(
            model=self.model, messages=messages
        )
        return response['choices'][0]['message']['content']