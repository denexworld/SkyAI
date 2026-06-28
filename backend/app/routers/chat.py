"""
SkyAI Chat Router
"""

def chat_route(message: str):
    return {
        "status": "success",
        "message": message,
        "reply": "Welcome to SkyAI! The AI engine will be connected soon."
    }
