from fastapi import FastAPI

app = FastAPI(
    title="AI Autonomous Research & Execution Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Autonomous Research & Execution Platform"
    }