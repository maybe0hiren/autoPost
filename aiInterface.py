from transformers import pipeline
def getCaption(taskList, modelPath="./capGenAI"):
    generator = pipeline("text-generation", model=modelPath, tokenizer=modelPath)
    tasksText = ", ".join(taskList)
    prompt = f"Tasks I Completed: {tasksText}. Today, "
    output = generator(prompt, max_length=50, num_return_sequences=1)
    return output[0]["generated_text"]
tasks = ["Practiced Data Structures and algorithms, Made a javascript website, finished an AclearI project"]
caption = getCaption(tasks)
print(caption)
