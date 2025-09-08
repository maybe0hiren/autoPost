import telebot
import os
import datetime
import requests

token = "TOKEN"
bot = telebot.TeleBot(token)
storage = "postContent"

def getData():
    today = datetime.date.today().strftime("%Y-%m-%d")
    folder = os.path.join(storage, today)
    os.makedirs(folder, exist_ok=True)
    return folder

def saveTasks(task):
    folder = getData()
    textFile = os.path.join(folder, "tasks.txt")
    with open(textFile, "a", encoding="utf-8") as f:
        f.write(f"{task.text}\n")

def saveImage(image):
    folder = getData()
    imageFile = image.photo[-1]
    info = bot.get_file(imageFile.file_id)
    imageURL = f"https://api.telegram.org/file/bot{token}/{info.file_path}"
    imageData = requests.get(imageURL).content
    imageName = f"img_{datetime.datetime.now().strftime('%H%M%S')}.jpg"
    imagePath = os.path.join(folder, imageName)
    with open(imagePath, "wb") as f:
        f.write(imageData)

@bot.message_handler(content_types=["text"])
def handleTasks(task):
    saveTasks(task)
    bot.reply_to(task, "📌 Task saved for today!")

@bot.message_handler(content_types=["photo"])
def handleImage(image):
    saveImage(image)
    bot.reply_to(image, "📷 Image saved for today!")

print("Bot running...")
bot.polling()

