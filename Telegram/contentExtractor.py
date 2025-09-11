import telebot
import os
import datetime
import requests

token = "TOKEN"
bot = telebot.TeleBot(token)
storage = "postContent"

def getBot():
    return bot

def getData():
    today = datetime.date.today().strftime("%Y-%m-%d")
    folder = os.path.join(storage, today)
    os.makedirs(folder, exist_ok=True)
    return folder

def saveTasks(task):
    folder = getData()
    textFile = os.path.join(folder, "tasks.txt")
    with open(textFile, "a", encoding="utf-8") as f:
        f.write(f"{task.text[6:]}\n")
    print(f"Successfully added -- {task.text[6:]}")

def saveEditedCaption(caption):
    folder = getData()
    textFile = os.path.join(folder, "caption.txt")
    with open(textFile, "w", encoding="utf-8") as f:
        f.write(f"{caption.text[10:]}\n")
    print(f"New Caption Saved: \n {caption.text[10:]}")

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
