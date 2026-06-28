"""
SkyAI Backend Entry Point
"""

from backend.app.core.settings import settings

def start():
    print("=" * 40)
    print(f"🚀 {settings.APP_NAME}")
    print(f"Version : {settings.VERSION}")
    print("Backend  : Ready")
    print("=" * 40)

if __name__ == "__main__":
    start()
