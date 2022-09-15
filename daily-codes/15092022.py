from gensim import models
import numpy as np
from gensim import corpora
from gensim.utils import simple_preprocess

documents = ["This is the first line",
             "This is the second sentence",
             "This third document"]

# Create the Dictionary and Corpus
mydict = corpora.Dictionary([simple_preprocess(line) for line in documents])
corpus = [mydict.doc2bow(simple_preprocess(line)) for line in documents]

#show weights 
print("Weights, raw:\n")
for doc in corpus:
    print([[mydict[id], freq] for id, freq in doc])

tfidf = models.TfidfModel(corpus, smartirs='ntc')
print("TFIDF Weights:\n")
for doc in tfidf[corpus]:
    print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])