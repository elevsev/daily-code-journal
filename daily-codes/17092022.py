from FUNCTIONS.data_functions import load_data, lemmatisation, write_data

import json
import glob
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import spacy
from nltk.corpus import stopwords

import pyLDAvis
import pyLDAvis.gensim_models

# def read_write_data(input_file_location='/Users/Kerryn/daily-code-journal/daily-codes/DATA/ushmm_dn.json', output_file_location='/Users/Kerryn/daily-code-journal/daily-codes/DATA/lemmatised_data_ushmm.json'):
#     data = load_data(input_file_location)['texts']
#     lemmatised_data = lemmatisation(texts=data)
#     write_data(file=output_file_location,data=lemmatised_data)
#     return lemmatised_data

# data = load_data('/Users/Kerryn/daily-code-journal/daily-codes/DATA/ushmm_dn.json')['texts']

# lemmatised_data = lemmatisation(texts=data)
# print(lemmatised_data[1][0:100])


# write_data(
#     file='/Users/Kerryn/daily-code-journal/daily-codes/DATA/lemmatised_data_ushmm.json',
#     data=lemmatised_data
#     )


lemmatised_data = load_data(file="/Users/Kerryn/daily-code-journal/daily-codes/DATA/lemmatised_data_ushmm.json")

def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final.append(new)
    return final

data_words = gen_words(lemmatised_data)
print(data_words[1][0:20])