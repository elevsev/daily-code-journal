import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from FUNCTIONS import data_functions
from FUNCTIONS.data_functions import KMeansForTRC

trc_kmeans = KMeansForTRC()
terms = trc_kmeans.terms
print(terms[0])