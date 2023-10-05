from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatjpt import ArabicChatBot

app = FastAPI(title="ChatBot using FastAPI")

class ChatBotInput(BaseModel):
    query: str

chat_bot = ArabicChatBot()

@app.post("/get_response/")
async def get_chatbot_response(chat_input: ChatBotInput):
    try:
        response = chat_bot.run(chat_input.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": "Internal Server Error", "message": str(e)})
