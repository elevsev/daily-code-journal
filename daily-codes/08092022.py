from tkinter import N
from FUNCTIONS import data_functions
from sklearn.cluster import KMeans

cleaned_docs = data_functions.get_trc_data()
# print(cleaned_docs[0])

vectorised = data_functions.Vectorisation(docs=cleaned_docs)
# print(vectorised.dense_list[0])
trc_vectors = vectorised.vectors

true_k = 20

model = KMeans(
    n_clusters=true_k, 
    init="k-means++", 
    max_iter=100,
    n_init=1
    )

model.fit(trc_vectors)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorised.feature_names

# with open("/Users/Kerryn/daily-code-journal/daily-codes/DATA/trc_results.txt", "w", encoding='utf-8') as f:
#     for i in range(true_k):
#         f.write(f"Cluster: {i}")
#         f.write("\n")
#         for order in order_centroids[i, :10]:
#             f.write(' %s' % terms[order],)
#             f.write("\n")
#         f.write("\n")
#         f.write("\n")

for i in range(true_k):
    print(f"Cluster {i}\n")
    for order in order_centroids[i, :5]:
        print(terms[order])
        # print('\n')
    print('\n')
    # print('\n')

        