#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(0)

class instance(object):
    def __init__(self, label, features):
        self.name = label
        self.features = features
        self.current_group = 0
        self.current_distance = np.inf

    def set_group(self, group):
        self.current_group = group

    def get_distance(self):
        return self.current_distance

    def get_group(self):
        return self.group

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + ' ' + str(self.features)

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
        plant_list = []
        for plant in data:
            temp_plant = instance(plant[0], plant[1:])
            plant_list.append(temp_plant)
        plant_list = np.asarray(plant_list)
        np.random.shuffle(plant_list)
        centroids = data[:k]
        while True:
            pass

def main():
    data = pd.read_csv('../data/plant_data_features.csv', header=0, index_col=False)
    data = data.values

    cluster = k_cluster(data, 10)

if __name__ == '__main__':
    main()
