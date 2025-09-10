from transformers import pipeline
def getCaption(taskList, modelPath="./capGenAI"):
    generator = pipeline("text-generation", model=modelPath, tokenizer=modelPath)
    tasksText = "; ".join(taskList)
    prompt = f"Tasks: {tasksText} Caption: "
    output = generator(prompt, max_length=250, do_sample=True, top_p=0.95, num_return_sequences=1)
    caption = output[0]['generated_text']
    if caption.startswith(prompt):
        return caption[len(prompt):].strip()
    else:
        return caption.strip()

tasks = ["Practiced Data Structures and algorithms, Made a website using javascript, started an AI project"]
caption = getCaption(tasks)
print(caption)
