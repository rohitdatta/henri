import numpy as n

''' implementation of kmeans
	centroids, C = kmeans(features, k)
	centroids = arrays of features corresponding to centroids
	C = matrix of indexes corresponding to closest centroid
'''
def kmeans(features, k, num_iterations = 10, plot_progress = None):
	centroids = features[n.random.choice(n.arange(len(features)), k), :]
	for i in range(num_iterations):
		cluster = n.array([n.argmin([n.dot(x_i - y_k, x_i - y_k) for y_k in centroids]) for x_i in features])
		centroids = [features[cluster == k].mean(axis = 0) for k in range(k)]
		if plot_progress != None: plot_progress(features, cluster, n.array(centroids))
		return n.array(centroids), cluster