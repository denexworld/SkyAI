"""
SkyAI Authentication Service
"""

class AuthService:

    def login(self, username, password):
        if username == "admin" and password == "1234":
            return {
                "success": True,
                "message": "Login successful"
            }

        return {
            "success": False,
            "message": "Invalid username or password"
        }
