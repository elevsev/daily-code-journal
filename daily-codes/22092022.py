from FUNCTIONS.data_functions import remove_stops
from nltk.corpus import stopwords

text = """Gensim = “Generate Similar” is a popular open source natural language processing (NLP) library used for unsupervised topic modeling. It uses top academic models and modern statistical machine learning to perform various complex tasks such as −

Building document or word vectors
Corpora
Performing topic identification
Performing document comparison (retrieving semantically similar documents)
Analysing plain-text documents for semantic structure
Apart from performing the above complex tasks, Gensim, implemented in Python and Cython, is designed to handle large text collections using data streaming as well as incremental online algorithms. This makes it different from those machine learning software packages that target only in-memory processing."""

# final = gen_words(texts=text)
# print(final)

stopwords = stopwords.words('english')
clean = remove_stops(text=text, stops=stopwords)
print(clean)