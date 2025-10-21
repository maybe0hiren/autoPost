from dotenv import load_dotenv
from google import genai
from supabase import create_client, Client

import os
import json
import datetime
import time
import requests


load_dotenv()
geminiKey = os.getenv("GEMINI_API_KEY")
supabaseURL = os.getenv("SUPABASE_URL")
supabaseKey = os.getenv("SUPABASE_KEY")
ayshareKey = os.getenv("AYSHARE_KEY")
supabase : Client = create_client(supabaseURL, supabaseKey)



def getCaption(prompt):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents= prompt
    )
    return response.text


def getPostContent():
    # today = datetime.date.today().strftime("%Y-%m-%d")
    # folderName = datetime.date.today().strftime("%Y-%m-%d")
    # os.makedirs(f"content/{folderName}", exist_ok=True)
    # print(f"Saving Images... to content/{folderName}")
    response = supabase.table("postContent").select("*").execute()
    if not response.data:
        print(f"Fetching Failed: {response}")
        return []
    rows = response.data or []
    tasks = []
    # imageCounter = 1
    
    for row in rows:
        task = row.get("task")
        # imageURL = row.get("imageURLs") or []
        # try:
        #     imageURL = json.loads(imageURL)
        # except json.JSONDecodeError:
        #     imageURL = []

        if task and task.strip():
            tasks.append(task.strip())

        # for url in imageURL:
        #     if not url or not isinstance(url, str):
        #         continue
        
            # extension = os.path.splitext(url)[1] or ".jpg"
            # imageName = f"image{imageCounter}{extension}"
            # imagePath = f"content/{today}/{imageName}"

            # try:
            #     response = requests.get(url, timeout=10)
            #     if response.status_code == 200:
            #         # with open(imagePath, "wb") as f:
            #         #     f.write(response.content)
            #         # print(f"Downloaded {imageName}")
            #         # imageCounter += 1
            #     else:
            #         print(f"Download Failed: {response.status_code}")
            # except Exception as e:
            #     print(f"Error downloading image: {e}")
    # print(f"\nDownload complete! {imageCounter-1} images saved in '{today}' folder.")
    supabase.table("postContent").delete().neq("id", 0).execute()
    print(f"Tasks found: {len(tasks)}")
    return tasks

def getDay():
    with open("day.txt", "r") as f:
        content = f.read().strip()
    num = int(content)
    with open("day.txt", "w") as f:
        f.write(str(num + 1))
    return str(num)

def postToX(caption):
    url = "https://app.ayrshare.com/api/post"
    headers = {
        "Authorization": f"Bearer {ayshareKey}",
        "Content-Type": "application/json"
    }
    # try:
    #     supported_ext = ('.jpg', '.jpeg', '.png')
    #     all_images = [f for f in os.listdir(folder) if f.lower().endswith(supported_ext)]
    # except FileNotFoundError:
    #     all_images = []
    # if len(all_images) > 4:
    #     selected_images = random.sample(all_images, 4)
    # else:
    #     selected_images = all_images
    # mediaUrls = [os.path.join(image_folder, img) for img in selected_images] if selected_images else []

    data = {    
        "post": caption,
        "platforms": ["twitter"]
    }
    # if mediaUrls:
    #     data["mediaUrls"] = mediaUrls

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"{response.json()}\n")

def alternateDayCheck(start_date):
    days_elapsed = (datetime.date.today() - start_date).days
    return days_elapsed % 2 == 0

def scheduler():
    start_date = datetime.date.today() - datetime.timedelta(days=1)
    print("AutoPoste running... will post every alternate day at 10:00 PM.\n")

    while True:
        now = datetime.datetime.now()
        target_time = now.replace(hour=22, minute=0, second=0, microsecond=0)

        if now >= target_time:
            target_time += datetime.timedelta(days=1)

        seconds_until_target = (target_time - now).total_seconds()
        print(f"Sleeping {int(seconds_until_target)}s until next check at {target_time.strftime('%Y-%m-%d %H:%M:%S')}...")
        time.sleep(seconds_until_target)

        if alternateDayCheck(start_date):
            print(f"\n[{datetime.datetime.now()}] Running task for today...\n")
            mainFunction()
        else:
            print(f"\n[{datetime.datetime.now()}] Skipping today (alternate day rule).\n")
        time.sleep(60)

def mainFunction():
    tasks = getPostContent()
    caption = "NOTHING TODAY!"
    if(tasks != []):
        tasks = ", ".join(tasks)
        prompt = "I like journaling about my Computer Science Engineering self learning journey on twitter and instagram and also sometimes about how I am feeling about the day... Keep it breif but well explained caption for the posts also add one or two relevant emojis. Add hashtags mid sentences, don't bunch them at the end. Most of the times they are about webdev projects and theory, android development projects and theory, Artificial Intelligent projects and theory.... here are the tasks I did today: " + tasks + " The character limit is 230....Just give me 1 final well thought caption and nothing else... No Options, No reasoning nothing else if there are no tasks"
        caption = getCaption(prompt)
        caption = f"Day {getDay()} " + caption
        postToX(caption)
        print(f"Posted: {caption} to twitter!")

if __name__ == "__main__":
    scheduler()