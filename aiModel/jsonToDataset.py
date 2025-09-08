import json 
from datasets import Dataset 

def getDataset():
    with open("captions.json", "r") as f:
        data = json.load(f)
    captionList = list(data.values())
    dataset = Dataset.from_dict({"text": captionList})
    print(f"loaded {len(dataset)} captions")
    return dataset