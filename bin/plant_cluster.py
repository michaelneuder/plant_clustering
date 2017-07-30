#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(0)

class k_cluster(object):
    def __init__(self, data, k):
        self.clusters = self.get_clusters(data, k)

    def get_euclidean_distance(self, x, y):
        if len(x) != len(y):
            raise ValueError('x and y need same dimension to find distance')
        else:
            sum_diffs = 0
            for i in range(len(x)):
                sum_diffs += (x[i]-y[i])**2
            return(np.sqrt(sum_diffs))

    def get_clusters(self, data, k):
        # np.random.shuffle(data)
        centroids = data[:k]
        # print(centroids)
        # while True:

def main():
    data = pd.read_csv('../data/plant_data_features.csv', header=0, index_col=False)
    data = data.values

    cluster = k_cluster(data, 1)

if __name__ == '__main__':
    main()
