import telebot 
from telebot import types
import time
import threading

BOT_TOKEN='7610428366:AAGBArawMIxFHss2yikBIoOn3xEWqdFSvww'
bot=telebot.TeleBot(BOT_TOKEN)
user_quanitity={}
user_remind={}
user_status={}


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add("1 Liter","2 Liter", "3 Liter")
    bot.send_message(message.chat.id,'выберите количество воды в сутки',reply_markup=markup)
    bot.register_next_step_handler(message,set_quanitity)
    
def set_quanitity(message):
    choise=message.text.strip()
    if choise not  in ["1 Liter","2 Liter", "3 Liter"]:
        bot.send_message(message.chat.id, "Неверный выбор попробуйте еще раз /start")
        return
    user_quanitity[message.chat.id]=int(choise.split()[0])*1000
    user_status[message.chat.id]=0
    bot.send_message(message.chat.id,f"Установлена суточная норма воды {choise}")
    bot.send_message(message.chat.id,"Чтобы бот отправлял вам напоминание о воде напишите /setreminder и время.\nНапример /setreminder 1  будет напоминать вам пить воду каждый час\nИ напиши /drunk 300(если выпил 300мл воды)")
        
@bot.message_handler(commands=['setreminder'])
def set_reminder(message):
    try:
        remind= int(message.text.split()[1])
    except (IndexError,ValueError):
        bot.send_message(message.chat.id, " укажите время правильно вот так /setreminder 1")
        return
    user_remind[message.chat.id]= remind
    bot.send_message(message.chat.id, f"напоминание о воде установлено {remind}")
    
    def cycle_remind(chat_id,remind ):
        while True:
            if chat_id in user_status and chat_id in user_quanitity:
                if user_status[chat_id]>=user_quanitity[chat_id]:
                    bot.send_message(chat_id, "вы выполнили дневную норму ")
                    break   
            time.sleep(remind *10)
            bot.send_message(chat_id, "не забудьте выпить воду")
            
    t=threading.Thread(target=cycle_remind, args=(message.chat.id,remind), daemon=True)
    t.start()
    
@bot.message_handler(commands=['drunk'])
def user_progress(message):
    try:
        amount=int(message.text.split()[1])
    except (IndexError,ValueError):
        bot.send_message(message.chat.id,"напишите без ошибок вот так /drunk и количество выпитой воды")
        return
    if message.chat.id not in  user_status:
        bot.send_message(message.chat.id, "Выберите дневную норму воды")
        return
    
    user_status[message.chat.id] += amount  
    user_goal=user_quanitity[message.chat.id]
    progress1=user_status[message.chat.id]
    if progress1>=user_goal:
        bot.send_message(message.chat.id,f"вы достигли своей цели выпить {user_goal}")
    else:
        left = user_goal - progress1
        bot.send_message(message.chat.id,f"вы выпили только {progress1} мл из {user_goal}. Осталось еще {left}мл выпить")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,'UNKNOWN COMMAND')
    
if __name__=='__main__':
    bot.polling()
