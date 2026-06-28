"""
SkyAI Message Model
"""

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def to_dict(self):
        return {
            "sender": self.sender,
            "content": self.content
        }

