import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aiModel.aiInterface import saveCaption
import telebot
import schedule
import time
import threading
from contentExtractor import saveTasks, saveImage, getBot, getData, saveEditedCaption


bot = getBot()

@bot.message_handler(content_types=["text"])
def handleTasks(task):
    if task.text.startswith("/task:"):
        saveTasks(task)
        bot.reply_to(task, "📌 Task saved for today!")
    elif task.text.startswith("/remake"):
        tasks = loadTasks()
        caption = saveCaption(tasks)
        sendCaption(caption)     
    elif task.text.startswith("/caption:"):
        saveEditedCaption(task)
        bot.reply_to(task, "✅ New Caption Saved!")
    else:
        validCommandsMessage = f"🚫OOPS! That message is out of my scope of understanding!\nHere's the list of valid commands:\n/task: to add a task you did in the dat\n/remake to remake a caption that didnt meet your expectations\n/caption: to save your edited caption into the database"
        bot.send_message(5731423209, validCommandsMessage)


@bot.message_handler(content_types=["photo"])
def handleImage(image):
    saveImage(image)
    bot.reply_to(image, "📷 Image saved for today!")

@bot.message_handler(commands=['start'])
def sendCaption(caption):
    bot.send_message(5731423209, " 📝 Here's today's Caption: \n" + caption)
    print("Caption Sent...")

def loadTasks():
    tasks = []
    folder = getData()
    textFile = os.path.join(folder, "tasks.txt")
    if not os.path.exists(textFile):
        with open(textFile, 'w') as f:
            pass
    with open(textFile, 'r', encoding="utf-8") as f:
        content = f.read()
    tasks = content.splitlines()
    print(f"Today's tasks: {tasks}")
    return tasks

def parent():
    tasks = loadTasks()
    caption = saveCaption(tasks)
    if(caption == ''):
        parent()
    sendCaption(caption)
    return 

print("Bot running...")
pollingThread = threading.Thread(target=bot.polling, daemon=True)
pollingThread.start()
schedule.every().day.at("01:10").do(parent)
while True:
    schedule.run_pending()
    time.sleep(10)