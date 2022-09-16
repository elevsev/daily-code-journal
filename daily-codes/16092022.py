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

from FUNCTIONS.data_functions import load_data, write_data

stopwords = stopwords.words('english')
# print(stopwords)

data = load_data("/Users/Kerryn/daily-code-journal/daily-codes/DATA/ushmm_dn.json")['texts']
## print(f"{data['RG'][0]}")

print('Raw text (first 100 characters):')
print(data[0][100])


def lemmatisation(texts, allowed_posttags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    texts_out = []
    for text in texts:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_posttags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    return texts_out

lemmatised_texts = lemmatisation(data)

print('Lemmatised text (first 100 characters):')
print(lemmatised_texts[0][0:100])