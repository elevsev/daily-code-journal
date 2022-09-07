import json
import nltk
from nltk.corpus import stopwords
import re 
import string


months_trc = [
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


def remove_stops(text, stops):
    '''Removes the case numbers of format AC/2---/1--'''
    text = re.sub(r"AC\/\d{1,4}\/\d{1,4}", "", text)
    words = text.split()
    final = []
    for word in words:
        if word not in stops:
            final.append(word)
    final = " ".join(final)
    final = final.translate(str.maketrans("", "", string.punctuation))
    final = "".join([i for i in final if not i.isdigit()])
    while "  " in final:
        final = final.replace("  ", " ")
    return (final)

def clean_docs(docs):
    stops = stopwords.words("english")
    months = months_trc
    stops = stops + months
    final = []
    for doc in docs:
        clean_doc = remove_stops(doc, stops)
        final.append(clean_doc)
    return final

