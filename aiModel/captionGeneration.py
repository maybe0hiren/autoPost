from jsonToDataset import getDataset
from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments
from transformers import pipeline

def tokenizeFunction(examples):
    token = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)
    token["labels"]=token["input_ids"].copy()
    return token

dataset = getDataset()
inputs = []
for entry in dataset:
    prompt = f"Tasks: {entry['tasks'].strip()} Caption:"
    target = entry['caption'].strip()
    fullText = prompt + " " + target
    inputs.append({"text" : fullText})

newDataset = Dataset.from_dict({"text" : [d["text"] for d in inputs]})

modelName = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(modelName)
model = GPT2LMHeadModel.from_pretrained(modelName)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    model.resize_token_embeddings(len(tokenizer))
tokenizedDataset = newDataset.map(tokenizeFunction, batched=True)
tokenizedDataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

trainingArgs = TrainingArguments(
    output_dir = "./capGenAI",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=2,
    save_steps=500,
    logging_steps=100,
    prediction_loss_only=True,
    fp16=False
)
trainer = Trainer(
    model=model,
    args=trainingArgs,
    train_dataset=tokenizedDataset
)
trainer.train()
trainer.save_model("capGenAI")
tokenizer.save_pretrained("capGenAI")
print("Model Trained")

# captionGenerator = pipeline("text-generation", model="capGenAI", tokenizer=tokenizer)
# output = captionGenerator("Today, ", max_length=50, num_return_sequences=1)

# print(output[0]["generated_text"])
