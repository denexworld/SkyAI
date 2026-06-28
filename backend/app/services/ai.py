"""
SkyAI AI Service
"""

class AIService:

    def generate_response(self, message):
        return {
            "success": True,
            "user_message": message,
            "ai_response": f"You said: {message}"
        }
