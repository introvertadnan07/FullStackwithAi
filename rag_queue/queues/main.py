from dotenv import load_dotenv
import uvicorn

from .server import app

load_dotenv()

def main():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
