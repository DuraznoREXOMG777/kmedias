import numpy as np
import matplotlib.pyplot as plotter
import brain

util = brain.Brain()
k = 7
data = np.genfromtxt("input.txt")
centroids = util.get_centroids(4, data)
errorList = []


def to_plot():
    distance_list = util.get_distance(data, centroids)
    errorList.append(util.get_error(distance_list, centroids))

    plotter.cla()
    plotter.plot(data[:, 0], data[:, 1], "k*")
    plotter.plot(centroids[:, 0], centroids[:, 1], "mo")
    plotter.show()


for i in range(0, k):
    to_plot()

plotter.cla()
plotter.plot(range(0, k + 1), errorList[:], "k*")
plotter.show()
