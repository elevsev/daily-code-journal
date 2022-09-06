from FUNCTIONS import data_functions
import pandas as pd
from nltk.corpus import stopwords
import re
import string

trc_file = "/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_dn.json"

months_trc = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

trc = data_functions.load_data(file=trc_file)
descriptions = trc['descriptions']
# print(descriptions)[0]

def remove_stops(text, stops):
    '''Removes the case numbers of format AC/2---/1--'''
    text = re.sub(r"AV\/\d{1,4}\/\d{1,4}", "", text)
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

cleaned_docs = clean_docs(descriptions)

print("Raw descriptions:\n")
print(descriptions[0])
print('\n--------------------------------------------------------------------------------------------------------------------\n')
print("Cleaned descriptions:\n")
print(cleaned_docs[0])
