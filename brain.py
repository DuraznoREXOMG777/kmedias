import numpy as np
import matplotlib.pyplot as plotter
import math


class Brain:

    def __init__(self):
        self.distance_sum = 0

    def get_centroids(self, num, array):
        if num <= len(array):
            amount = len(array) / num
            divided = str(amount).split('.')
            centroid_separation = int(divided[0])
            x_sum = 0
            y_sum = centroid_separation
            plotter.plot(array[:, 0], array[:, 1], "k*")
            x_list = []
            y_list = []
            for i in range(0, num):
                if i == num - 1 and int(divided[1]) != 0:
                    x = sum(array[x_sum:len(array), 0]) / len(array[x_sum:len(array), 0])
                    y = sum(array[x_sum:len(array), 1]) / len(array[x_sum:len(array), 1])
                    x_list.append(x)
                    y_list.append(y)
                    plotter.plot(x, y, "mo")
                else:
                    x = sum(array[x_sum:y_sum, 0]) / centroid_separation
                    y = sum(array[x_sum:y_sum, 1]) / centroid_separation
                    x_list.append(x)
                    y_list.append(y)
                    plotter.plot(x, y, "mo")
                    x_sum += centroid_separation
                    y_sum += centroid_separation
            centroids_array = np.column_stack([x_list[:], y_list[:]])
            return centroids_array

        else:
            print("Can't generate " + str(num) + " centroids with " + str(len(array)) + " coordinates.")

    def get_distance(self, data, centroids):
        distance_list = []
        for i in range(0, len(centroids)):
            distance_centroid_a = []
            for j in range(0, len(data)):
                a = (data[j][0] - centroids[i][0]) ** 2
                b = (data[j][1] - centroids[i][1]) ** 2
                c = math.sqrt(a + b)
                distance_centroid_a.append(c)
            distance_list.append(distance_centroid_a)

        return distance_list

    def less_distance_to_centroid(self, distance_list):
        dominant_centroids = []
        for i in range(0, len(distance_list[0])):
            first = True
            for j in range(0, len(distance_list)):
                if (first):
                    value_to_compare = distance_list[j][i]
                    predomintant_crentroid = j
                if value_to_compare > distance_list[j][i] and not first:
                    value_to_compare = distance_list[j][i]
                    predomintant_crentroid = j

                first = False

            dominant_centroids.append(predomintant_crentroid)

        return dominant_centroids

    def new_centroids(self, dominant_centroids_list, len_centroids, data):
        x_new_centroids = []
        y_new_centroids = []
        for i in range(0, len_centroids):
            x_counter = 0
            y_counter = 0
            x_sum = 0
            y_sum = 0
            for j in range(0, len(data)):
                if dominant_centroids_list[j] == i:
                    x_counter += 1
                    y_counter += 1
                    x_sum += data[j][0]
                    y_sum += data[j][1]
            x = x_sum / x_counter
            y = y_sum / y_counter
            x_new_centroids.append(x)
            y_new_centroids.append(y)
        centroids = np.column_stack([x_new_centroids[:], y_new_centroids[:]])
        return centroids

    def get_error(self, distance_list, centroids):
        error_list = []
        counter_list = []

        for i in range(0, len(centroids)):
            error_list.append(0)
            counter_list.append(0)

        for i in range(0, len(distance_list[0])):
            first = True
            for k in range(0, len(distance_list)):
                if (first):
                    value_to_compare = distance_list[k][i]
                    predominant_centroid = k
                if value_to_compare > distance_list[k][i] and not first:
                    value_to_compare = distance_list[k][i]
                    predominant_centroid = k

                first = False

            sum = error_list[predominant_centroid]
            sum += value_to_compare
            error_list[predominant_centroid] = sum
            error_sum = counter_list[predominant_centroid]
            error_sum += 1
            counter_list[predominant_centroid] = error_sum
        error = 0

        for l in range(0, len(error_list)):
            error += error_list[l] / counter_list[l]
        error = error / len(centroids)

        return error

    def get_new_error(self, dominant_centroid_list, distance_list, centroids):
        error = 0
        error_list = []
        counter_list = []

        for i in range(0, len(centroids)):
            error_list.append(0)
            counter_list.append(0)

        for i in range(0, len(dominant_centroid_list)):
            distance = distance_list[dominant_centroid_list[i]][i]

            sum = counter_list[dominant_centroid_list[i]]
            sum += distance
            counter_list[dominant_centroid_list[i]] = sum

            error_list[dominant_centroid_list[i]] = error_list[dominant_centroid_list[i]] + 1

        for l in range(0, len(error_list)):
            error += counter_list[l] / error_list[l]
            error = error
        return print(error)
