import os
import numpy as np
import pandas as pd

class DataSets:
    @staticmethod
    def add_bias(arr, bias = -1):
        biased_arr = np.ndarray(shape=(arr.shape[0], arr.shape[1]+1), dtype=float)
        for i in range(0, len(arr)):
            biased_arr[i] = np.append(bias, arr[i])

        return biased_arr


class TESTE:
    teste = pd.read_csv("dataset/dataset_1.csv")
    input = [teste.sepal_largura, teste.sepal_comprimento]
    output = [teste.tipo]
    input = DataSets.add_bias(input)