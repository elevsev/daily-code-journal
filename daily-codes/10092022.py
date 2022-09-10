import matplotlib.pyplot as plt
from FUNCTIONS.data_functions import KMeansForTRC, PCAForTRC, Vectorisation, get_trc_data

#pipeline 

names = Vectorisation(docs=get_trc_data())
names = names.feature_names
kmeans = KMeansForTRC()
pca_vectors = kmeans.trc_vector_array
print(len(kmeans.kmeans_indices))

trc_pca = PCAForTRC(pca_vectors=pca_vectors)
print(trc_pca.scatter_plot_points[0:5])

colours_per_cluster = ['r', 'b', 'g', 'y']

x_axis = [x[0] for x in trc_pca.scatter_plot_points]
y_axis = [y[1] for y in trc_pca.scatter_plot_points]

fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, c=[colours_per_cluster[d] for d in kmeans.kmeans_indices])

for i, txt in enumerate(names):
    ax.annotate(txt[0:5], (x_axis[i], y_axis[i]))

plt.show()