from jsonToDataset import getDataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments
from transformers import pipeline

def tokenizeFunction(examples):
    token = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)
    token["labels"]=token["input_ids"].copy()
    return token

dataset = getDataset()

modelName = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(modelName)
model = GPT2LMHeadModel.from_pretrained(modelName)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizedDataset = dataset.map(tokenizeFunction, batched=True)
tokenizedDataset = tokenizedDataset.remove_columns(["text"])
tokenizedDataset = tokenizedDataset.with_format("torch")

trainingArgs = TrainingArguments(
    output_dir = "./capGenAI",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
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

# captionGenerator = pipeline("text-generation", model="capGenAI", tokenizer=tokenizer)
# output = captionGenerator("Today, ", max_length=50, num_return_sequences=1)

# print(output[0]["generated_text"])
