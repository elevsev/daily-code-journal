import gensim
from FUNCTIONS.data_functions import gen_words, load_data


data = "/Users/Kerryn/daily-code-journal/daily-codes/DATA/lemmatised_data_ushmm.json"

lemmatised_data = gen_words(texts=load_data(data))
print(lemmatised_data[0][:100])

bigram_phrases = gensim.models.Phrases(
    lemmatised_data, 
    min_count=5,
    threshold=100
    )
trigram_phrases = gensim.models.Phrases(
    bigram_phrases[lemmatised_data], 
    threshold=100
    )
print(bigram_phrases)


#BIGRAMS AND TRIGRAMS

bigram = gensim.models.phrases.Phraser(bigram_phrases)
trigram = gensim.models.phrases.Phraser(trigram_phrases)

def make_bigrams(texts):
    return([bigram[doc] for doc in texts])

def make_trigrams(texts):
    return ([trigram[bigram[doc]] for doc in texts])

data_bigrams = make_bigrams(lemmatised_data)
data_bigrams_trigrams = make_trigrams(data_bigrams)

print(data_bigrams_trigrams[0][0:20])