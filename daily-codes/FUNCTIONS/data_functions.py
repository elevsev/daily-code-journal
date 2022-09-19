import json
import nltk
from nltk.corpus import stopwords
import re 
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import spacy
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

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


def get_trc_data(trc_file="/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_dn.json"):
    trc = load_data(file=trc_file)
    descriptions = trc['descriptions']
    return descriptions 

class CleanTRC:
    def __init__(self):
        self.descriptions = get_trc_data()
        self.cleaned_docs = clean_docs(self.descriptions)

class Vectorisation:
    def __init__(self, docs=CleanTRC().cleaned_docs, *args, **kwargs):
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
        self.docs = docs
        self.vectors = self.vectoriser.fit_transform(docs)
        self.feature_names = self.vectoriser.get_feature_names_out()
        self.dense = self.vectors.todense()
        self.dense_list = self.dense.tolist()


class KMeansForTRC:
    def __init__(self, true_k=20):
        '''Creates the pipeline for KMeans.
        ** PARAMS **
        true_k: number of clusters (default set to 20)

        ** ATTRIBUTES ** 
        docs: cleaned TRC docs
        true_k: number of clusters
        model: KMeans with pre-set parameters
        trc_vectorised: vectorised version of docs
        '''
        self.docs = get_trc_data()
        self.docs = clean_docs(docs=self.docs)
        self.true_k = true_k
        self.model = KMeans(
            n_clusters=self.true_k, 
            init="k-means++", 
            max_iter=100,
            n_init=1
            )
        self.trc_vectorised = Vectorisation()
        self.trc_vectors = self.trc_vectorised.vectors
        self.trc_vector_array = self.trc_vectors.toarray()

        self.model.fit(self.trc_vectorised.vectors)
        self.order_centroids = self.model.cluster_centers_.argsort()[:, ::-1]
        self.terms = self.trc_vectorised.feature_names 
        self.kmeans_indices = self.model.fit_predict(self.trc_vectors)


class PCAForTRC():
    def __init__(self,pca_vectors=KMeansForTRC().trc_vector_array, n_components=2):
        self.pca_vectors = pca_vectors
        self.pca = PCA(n_components=n_components)
        self.scatter_plot_points = self.pca.fit_transform(self.pca_vectors)

    # kmeans_indices = KMeansForTRC().kmeans_indicess

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

def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final.append(new)
    return final

class LDASetUp:
    def __init__(self, data):
        self.lemmatised_data = gen_words(texts=load_data(data))
        self.id2word = corpora.Dictionary(self.lemmatised_data)
        
        self.corpus = []
        for text in self.lemmatised_data:
            new = self.id2word.doc2bow(text)
            self.corpus.append(new)

    def lda_model(self):
        self.lda_model = gensim.models.ldamodel.LdaModel(
        corpus=self.corpus,
        id2word=self.id2word,
        num_topics=30,
        random_state=100,
        update_every=1,
        chunksize=100,
        passes=10,
        alpha='auto'
        )
