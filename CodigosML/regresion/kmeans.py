#importing Numpy,matplotlib and sklearn libraries

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use("ggplot")

#que tipo de machine learning usaremos
from sklearn.cluster import KMeans

#Preprocesamiento 
x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show()

#like we did before, convertir nuestra adata to a numpy array
x = np.array([[1,2], [5,8], [1,5,1,8], [8,8], [1,0,6], [9,11]])

#initialize the k-means algorithm
kmeans = KMeans('n_cluster=2')
kmeans.fit(x)

#getting the values of centroids and labels based on the fitment

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
print('************************')
print(type(centroids))
print(type(labels))

#plotting and visualization of output

colors = ["g", "r", "c", "y"]

for i in range(len(x)):
    print('coordinate:',X[i], 'label:', labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], makersize = 10)

plt.scatter(centroids[:, 0], centroids[:, 1], maker = 'x', s=150, linewidths = 5, zorder = 10)

plt.show()


