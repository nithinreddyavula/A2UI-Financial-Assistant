from fastapi import FastAPI

from app.models.chat import ChatRequest

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "A2UI Financial Assistant Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    return {
        "response": f"Received your message: {request.message}"
    }