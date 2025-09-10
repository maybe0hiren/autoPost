from transformers import pipeline
import os
import datetime

def saveCaption(taskList, modelPath="./capGenAI"):
    generator = pipeline("text-generation", model=modelPath, tokenizer=modelPath)
    tasksText = "; ".join(taskList)
    prompt = f"Tasks: {tasksText} Caption: "
    output = generator(prompt, max_length=250, do_sample=True, top_p=0.95, num_return_sequences=1)
    caption = output[0]['generated_text']
    if caption.startswith(prompt):
        caption = caption[len(prompt):].strip()
    else:
        caption = caption.strip()
    print(caption)

    storage = "postContent"
    today = datetime.date.today().strftime("%Y-%m-%d")
    folder = os.path.join(storage, today)
    os.makedirs(folder, exist_ok=True)
    folder = os.path.join(storage, today)
    captionFile = os.path.join(folder, "caption.txt")
    with open(captionFile, "a", encoding="utf-8") as f:
        f.write(caption)

tasks = ["Completed a course", "Learnt python", "Dance practice", "Conjuring"]
saveCaption(tasks)


