from flask import Flask, request, jsonify
from ChatFrompin import ArabicChatBot
app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json['data']  # تحصل هنا على البيانات المرسلة من التطبيق Flutter

    response_jpt=ArabicChatBot()
    qeury=response_jpt.run(data)
    # تستعد لإرسال البيانات الأخرى إلى التطبيق Flutter
    print(qeury)
    response_data = {'result': qeury}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=Flase,host='0.0.0.0', port=5000)










# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}




# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from chatjpt import ArabicChatBot

# app = FastAPI(title="ChatBot using FastAPI")

# class ChatBotInput(BaseModel):
#     query: str

# chat_bot = ArabicChatBot()

# @app.post("/get_response/")
# async def get_chatbot_response(chat_input: ChatBotInput):
#     try:
#         response = chat_bot.run(chat_input.query)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail={"error": "Internal Server Error", "message": str(e)})
