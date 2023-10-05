# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import uvicorn
# from chatjpt import ArabicChatBot

# app = FastAPI(title="Upload using FastAPI")

# class ChatBotInput(BaseModel):
#     query: str

# chat_bot = ArabicChatBot()

# @app.post("/get_response/{chat_input.query}")
# async def get_chatbot_response(chat_input: ChatBotInput):
#     try:
#         response = chat_bot.run(chat_input.query)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from chatjpt import ArabicChatBot
g=ArabicChatBot()
print(g.run("ماهي جامعة الرازي"))
