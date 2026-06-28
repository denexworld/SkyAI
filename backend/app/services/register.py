"""
SkyAI Registration Service
"""

class RegisterService:

    def register(self, username, email, password):
        return {
            "success": True,
            "user": {
                "username": username,
                "email": email
            },
            "message": "User registered successfully."
        }
