from backend.app.core.config import APP_NAME, VERSION
def start():
    print("=" * 40)
    print(f"{APP_NAME}")
    print(f"Version: {VERSION}")
    print("Status: Development")
    print("=" * 40)

if __name__ == "__main__":
    start()
