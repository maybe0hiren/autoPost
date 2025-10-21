from dotenv import load_dotenv
from google import genai
from supabase import create_client, Client

import os
import json
import datetime
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
    today = datetime.date.today().strftime("%Y-%m-%d")
    folderName = datetime.date.today().strftime("%Y-%m-%d")
    os.makedirs(f"content/{folderName}", exist_ok=True)
    print(f"Saving Images... to content/{folderName}")
    response = supabase.table("postContent").select("*").execute()
    if not response.data:
        print(f"Fetching Failed: {response}")
        return []
    rows = response.data or []
    tasks = []
    imageCounter = 1
    
    for row in rows:
        task = row.get("task")
        imageURL = row.get("imageURLs") or []
        try:
            imageURL = json.loads(imageURL)
        except json.JSONDecodeError:
            imageURL = []

        if task and task.strip():
            tasks.append(task.strip())

        for url in imageURL:
            if not url or not isinstance(url, str):
                continue
        
            extension = os.path.splitext(url)[1] or ".jpg"
            imageName = f"image{imageCounter}{extension}"
            imagePath = f"content/{today}/{imageName}"

            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(imagePath, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded {imageName}")
                    imageCounter += 1
                    supabase.table("postContent").delete().neq("id", 0).execute()
                else:
                    print(f"Download Failed: {response.status_code}")
            except Exception as e:
                print(f"Error downloading image: {e}")

    print(f"\nDownload complete! {imageCounter-1} images saved in '{today}' folder.")
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

    data = {
        "post": caption,
        "platforms": ["twitter"]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"{response.json()}\n")



if __name__ == "__main__":
    tasks = getPostContent()
    caption = "NOTHING TODAY!"
    if(tasks != []):
        tasks = ", ".join(tasks)
        prompt = "I like journaling about my Computer Science Engineering self learning journey on twitter and instagram and also sometimes about how I am feeling about the day... Keep it breif but well explained caption for the posts also add one or two relevant emojis. Add hashtags mid sentences, don't bunch them at the end. Most of the times they are about webdev projects and theory, android development projects and theory, Artificial Intelligent projects and theory.... here are the tasks I did today: " + tasks + " The character limit is 230....Just give me 1 final well thought caption and nothing else... No Options, No reasoning nothing else if there are no tasks"
        caption = getCaption(prompt)
        caption = f"Day {getDay()} " + caption
        postToX(caption)
        print(f"Posted: {caption} to twitter!")
    