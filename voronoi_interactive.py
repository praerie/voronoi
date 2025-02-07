import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


# update the voronoi tessellation when the user clicks
def onclick(event):
    global points, title

    # check if click is inside the plot area
    if event.xdata is not None and event.ydata is not None:
        # add the clicked point to the points array
        points = np.vstack([points, [event.xdata, event.ydata]])

        ax.clear()  # clear the previous diagram

        vor = Voronoi(points)
        voronoi_plot_2d(vor, ax=ax, show_vertices=False)
        ax.set_title(title)

        # update point counter text box
        point_counter = ax.text(0.05, 0.95, f"Points: {len(points)}", transform=ax.transAxes,
                                fontsize=12, verticalalignment="top", bbox=dict(facecolor="white", alpha=0.7))

        plt.draw()  # redraw the updated plot


title = "Click to add a point to the tessellation"

# begin with 7 random 2D points
points = np.random.rand(7, 2)

# create the initial plot
fig, ax = plt.subplots()
vor = Voronoi(points)
voronoi_plot_2d(vor, ax=ax, show_vertices=False)
ax.set_title(title)

# connect the click event to the onclick function
fig.canvas.mpl_connect('button_press_event', onclick)

# display the interactive plot
plt.show()
