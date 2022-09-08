import json
import nltk
from nltk.corpus import stopwords
import re 
import string
from sklearn.feature_extraction.text import TfidfVectorizer

months_trc = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
            ]

class Months_TRC:
    def __init__(self):
        self.months_trc = [
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

# def vectorisation(docs,*args, **kwargs):
#     vectoriser = TfidfVectorizer(
#     lowercase=True,
#     max_features=100,
#     # threshold at 80%
#     max_df=0.8,
#     # if word doesn't occur at least five times, ignore
#     min_df=5,
#     # set ngram to be between 1 to 3 times
#     ngram_range=(1,3),
#     stop_words="english"
#     )

#     vectors = vectoriser.fit_transform(cleaned_docs)
#     feature_names = vectoriser.get_feature_names_out()
#     dense = vectors.todense()
#     dense_list = dense.tolist()


def get_trc_data(trc_file="/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_dn.json"):
    trc = load_data(file=trc_file)
    descriptions = trc['descriptions']
    return descriptions 

class Vectorisation:
    def __init__(self, docs, *args, **kwargs):
        self.vectoriser = TfidfVectorizer(
        lowercase=True,
        max_features=100,
        # threshold at 80%
        max_df=0.8,
        # if word doesn't occur at least five times, ignore
        min_df=5,
        # set ngram to be between 1 to 3 times
        ngram_range=(1,3),
        stop_words="english"
        )

        self.vectors = self.vectoriser.fit_transform(docs)
        self.feature_names = self.vectoriser.get_feature_names_out()
        self.dense = self.vectors.todense()
        self.dense_list = self.dense.tolist()