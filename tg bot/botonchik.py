import os
from google import genai
from google.genai import types
import telebot


BOT_TOKEN = "7610428366:AAGBArawMIxFHss2yikBIoOn3xEWqdFSvww"
GEMINI_API_KEY = "AIzaSyDiGxCPUser1rQdXVdnDGfVVE0hdah-z0w"


bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

generation_config = types.GenerateContentConfig(
    temperature=1,
    top_p=0.95,
    max_output_tokens=8192,
)

system_prompt = """
Ты — Ботик, помощник в Телеграме.
Отвечай спокойно, как доброжелательный ассистент.
Сначала объясняй и давай обучайющий материал по теме , потом предлогай готовое решение, если пользователь попросит.
"""


def create_chat():
    return {
        "history": [
            {
                "role": "user",
                "parts": [types.Part.from_text(text=system_prompt)],
            }
        ]
    }

chat_session = create_chat()


def send_to_gemini(user_text):
    chat_session["history"].append({
        "role": "user",
        "parts": [types.Part.from_text(text=user_text)],
    })
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=chat_session["history"],
            config=generation_config,
        )
    except:
        return f"ошибка запроса"
    
    reply_text=getattr(response,"text","нету ответа")
    chat_session["history"].append({
        "role": "model",
        "parts": [types.Part.from_text(text=response.text)],
    })
    return reply_text
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"привет напиши свои вопрос я тебе помогу")
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    reply = send_to_gemini(message.text)
    bot.reply_to(message, reply)

print("Ботик запущен")
bot.infinity_polling()