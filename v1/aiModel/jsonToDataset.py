import json 
from datasets import Dataset 

def getDataset():
    with open("captions.json", "r") as f:
        data = json.load(f)
    dataset = []
    for day, entry in data.items():
        dataset.append({
            "tasks" : entry["tasks"],
            "caption" : entry["caption"]
        })
    return dataset