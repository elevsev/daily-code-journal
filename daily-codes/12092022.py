# LDA: each document receives one topic whereas KMeans works with multiple

# https://radimrehurek.com/gensim/
# import gensim
# import gensim.corpora as corpora
# from gensim.utils import simple_preprocess
# from gensim.models import CoherenceModel

from collections import defaultdict

# GENSIM:
#Document: some text.
# Corpus: a collection of documents.
# Vector: a mathematically convenient representation of a document.
# Model: an algorithm for transforming vectors from one representation to another.

document = "Human machine interface for lab abc computer applications"

text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

stoplist = set('for a of the and to in'.split(' '))
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]

freq = defaultdict(int)
for text in texts:
    for token in text:
        freq[token] += 1

processed_corpus = [[token for token in text if freq[token] > 1] for text in texts]
print('Texts:')
print(texts)
print('\n')
print('Frequency:')
print(freq)
print('\n')
print('Processed corpus:')
print(processed_corpus)
