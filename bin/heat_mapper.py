#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_euclidean_distance(x, y):
    if len(x) != len(y):
        raise ValueError('x and y need same dimension to find distance')
    else:
        sum_diffs = 0
        for i in range(len(x)):
            sum_diffs += (x[i]-y[i])**2
        return(np.sqrt(sum_diffs))

def plot_heat_map(data):
    dim = 100
    distances = np.zeros([dim, dim])
    for plant1 in range(dim):
        for plant2 in range(dim):
            dist = get_euclidean_distance(data[plant1][1:], data[plant2][1:])
            distances[plant1, plant2] = dist
    plt.imshow(distances, cmap='terrain', interpolation='nearest')
    plt.colorbar()
    plt.show()

def main():
    data = pd.read_csv('../data/plant_data_features.csv', header=0, index_col=False)
    data = data.values
    plot_heat_map(data)

if __name__ == '__main__':
    main()
