"""
SkyAI Conversation Model
"""

class Conversation:
    def __init__(self, user, message):
        self.user = user
        self.message = message

    def to_dict(self):
        return {
            "user": self.user,
            "message": self.message
        }
