import json
import nltk
from nltk.corpus import stopwords

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def load_data(file):
    with open(file=file, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_data(file, data):
    with open(file=file, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return data

