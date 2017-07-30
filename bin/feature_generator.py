#!/usr/bin/env python3
import csv
import numpy as np

def main():
    with open('../data/abbreviations.csv', 'r') as read_csv:
        reader = csv.reader(read_csv, delimiter=' ')
        abbreviations = []
        for line in reader:
            abbreviations.append(line[0])
    read_csv.close()

    with open('../data/plant_data.csv', 'r') as read_csv:
        with open('../data/plant_data_features.csv', 'w') as write_csv:
            write_csv.write('species,')
            abb_string = ''
            for abb in abbreviations:
                abb_string += abb+','
            write_csv.write(abb_string[:-1]+'\n')
            reader = csv.reader(read_csv)
            for line in reader:
                write_csv.write(line[0]+',')
                feature_vector = np.zeros(len(abbreviations))
                for i in range(1,len(line)):
                    for j in range(len(abbreviations)):
                        if line[i] == abbreviations[j]:
                            feature_vector[j] = 1
                feature_string = ''
                for k in feature_vector:
                    feature_string += str(int(k))+','
                write_csv.write(feature_string[:-1])
                write_csv.write('\n')
        write_csv.close()
    read_csv.close()

if __name__ == '__main__':
    main()
