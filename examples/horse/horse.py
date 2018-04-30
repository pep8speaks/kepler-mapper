import numpy as np
import sklearn
import kmapper as km

data = np.genfromtxt('horse-reference.csv',delimiter=',')

mapper = km.KeplerMapper(verbose=2)


lens = mapper.fit_transform(data)


graph = mapper.map(lens,
                   data,
                   clusterer=sklearn.cluster.DBSCAN(eps=0.1, min_samples=5),
                   cover=km.Cover(30, 0.2))

mapper.visualize(graph,
                 path_html="horse_keplermapper_output.html",
                 custom_tooltips=np.arange(len(lens)))

# You may want to visualize the original point cloud data in 3D scatter too
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0],data[:,1],data[:,2])
plt.savefig("horse-reference.csv.png")
plt.show()
"""
