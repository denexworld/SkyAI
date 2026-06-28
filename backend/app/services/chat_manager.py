"""
SkyAI Chat Manager
"""

class ChatManager:
    def __init__(self):
        self.history = []

    def send_message(self, message):
        self.history.append({
            "user": message,
            "assistant": f"You said: {message}"
        })

        return self.history[-1]

    def get_history(self):
        return self.history
