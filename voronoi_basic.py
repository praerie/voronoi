import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# generate random points
points = np.random.rand(10, 2)  # 10 random 2D points

# compute the voronoi tessellation
vor = Voronoi(points)

# plot the voronoi tessellation
fig = voronoi_plot_2d(vor)
plt.title('Voronoi Tessellation')
plt.show()