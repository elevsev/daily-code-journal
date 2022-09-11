from turtle import color
import matplotlib.pyplot as plt
from FUNCTIONS.data_functions import KMeansForTRC, PCAForTRC, Vectorisation, get_trc_data

#pipeline 

names = Vectorisation()
names = names.feature_names

print(len(names))
kmeans = KMeansForTRC()
pca_vectors = kmeans.trc_vector_array
kmeans_indices = kmeans.kmeans_indices
print(len(pca_vectors))
print(len(kmeans_indices))
print(kmeans_indices[:5])

trc_pca = PCAForTRC()
scatter_points = trc_pca.scatter_plot_points
print(len(scatter_points))

colours_per_cluster = ['g', 'y']

x_axis = [x[0] for x in scatter_points]
y_axis = [y[1] for y in scatter_points]

for i, txt in enumerate(names):
    print(txt, (x_axis[i], y_axis[i]))

i = 0
for cluster in kmeans.order_centroids:
    print(f"Cluster: {i}")
    for keyword in cluster:
        print(kmeans.terms[keyword])
    print("")
    i += 1


# print(len(x_axis))
# print(len(y_axis))

# fig, ax = plt.subplots()
# ax.scatter(x_axis, y_axis, )

# for i, txt in enumerate(names):s
#     ax.annotate(txt[0:5], (x_axis[i], y_axis[i]))

# plt.show()