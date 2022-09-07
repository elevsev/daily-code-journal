from FUNCTIONS import data_functions
from sklearn.feature_extraction.text import TfidfVectorizer

def get_trc_data(trc_file="/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_dn.json"):
    trc = data_functions.load_data(file=trc_file)
    descriptions = trc['descriptions']
    return descriptions 

cleaned_docs = data_functions.clean_docs(docs=get_trc_data())
print(cleaned_docs[0])

vectoriser = TfidfVectorizer(
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

vectors = vectoriser.fit_transform(cleaned_docs)
feature_names = vectoriser.get_feature_names_out()
dense = vectors.todense()
dense_list = dense.tolist()

print(vectors[0])
print(feature_names[0])
print(dense[0])
print(dense_list[0])

all_keywords = []

for description in dense_list:
    x = 0
    keywords = []
    for word in description:
        if word > 0:
            keywords.append(feature_names[x])
        x += 1
    all_keywords.append(keywords)

print(all_keywords[0])