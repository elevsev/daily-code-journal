from ast import Pass
from FUNCTIONS.data_functions import load_data, lemmatisation, gen_words
import pyLDAvis
import pyLDAvis.gensim_models
import gensim.corpora as corpora
import gensim

data = "/Users/Kerryn/daily-code-journal/daily-codes/DATA/lemmatised_data_ushmm.json"

lemmatised_data = gen_words(texts=load_data(data))

id2word = corpora.Dictionary(lemmatised_data)

corpus = []
for text in lemmatised_data:
    new = id2word.doc2bow(text)
    corpus.append(new)

print("Tuple form of corpus: ")
print(corpus[0][:20])
print("First element of tuple as word: ")
print(id2word[[0][:1][0]])


# lda model
lda_model = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    id2word=id2word,
    num_topics=30,
    random_state=100,
    update_every=1,
    chunksize=100,
    passes=10,
    alpha='auto'
)