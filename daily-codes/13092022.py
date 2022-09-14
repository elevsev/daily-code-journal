from gensim import corpora
from collections import defaultdict

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

single_text = "Human machine interface for lab abc computer applications"

stoplist = set('for a of the and to in'.split(' '))
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in single_text.lower().split() if word not in stoplist]
         for single_text in text_corpus]

# Count word frequencies

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
print("Processed corpus:")
print(processed_corpus)
print("\nDictionary of processed corpus:")
corp_dict = corpora.Dictionary(processed_corpus)
print(corp_dict, "\n")
print("Token2ID:\n",corp_dict.token2id,"\n")

# creatin ga new bag-of-word representation for new phrase
new_phrase = "Human computer interaction"
print("New phrase:\n", new_phrase)
new_vec = corp_dict.doc2bow(new_phrase.lower().split())
print("New vector\n", new_vec)
# [(0, 1), (1, 1)] --> first entry, value; second entry, value

#converting to a list of vectors
bow_corpus = [corp_dict.doc2bow(text) for text in processed_corpus]
print("BoW corpus:\n", bow_corpus)