# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uNbA1A7oV36n1OOMnX-relBnPyD3Mwwf
"""

from google.colab import drive

drive.mount("/content/gdrive")

from numpy import genfromtxt

data_path = "/content/gdrive/My Drive/iris.csv"
my_data = genfromtxt(data_path, delimiter=",")

type(my_data)

data = my_data.tolist()
for i in range(5):
    print(data[i])
type(data)

Train_set = []
Val_set = []
Test_set = []

import random

random.shuffle(data)

for S in range(0, len(data)):
    R = random.uniform(0, 1)
    if R >= 0 and R <= 0.7:
        Train_set.append(data[S])
    elif R > 0.7 and R <= 0.85:
        Val_set.append(data[S])
    else:
        Test_set.append(data[S])

print("Train Set:", Train_set, "\n")
print("Validation Set:", Val_set, "\n")
print("Test Set:", Test_set, "\n")

import math
import numpy as np
from collections import Counter

correct = 0
validation_accuracy = 0
K = 15

for V in Val_set:
    Euclidean_distance = []
    for T in Train_set:
        distance = math.sqrt(
            pow(V[0] - T[0], 2)
            + pow(V[1] - T[1], 2)
            + pow(V[2] - T[2], 2)
            + pow(V[3] - T[3], 2)
        )
        Euclidean_distance.append([distance, T[4]])
    Euclidean_distance = sorted(Euclidean_distance)

    nearest_k_neighbour_List = []
    for x in range(K):
        nearest_k_neighbour_List.append(Euclidean_distance[x])
    nearest_k_neighbour_List = np.array(nearest_k_neighbour_List)

    majority = Counter(nearest_k_neighbour_List.flat).most_common(1)

    if majority[0][0] == V[4]:
        correct = correct + 1

validation_accuracy = (correct / len(Val_set)) * 100
print("Validation Accuracy: ", validation_accuracy)

test_accuracy = 0
correct = 0
K = 15

for V in Test_set:
    Euclidean_distance = []
    for T in Train_set:
        distance = math.sqrt(
            pow(V[0] - T[0], 2)
            + pow(V[1] - T[1], 2)
            + pow(V[2] - T[2], 2)
            + pow(V[3] - T[3], 2)
        )
        Euclidean_distance.append([distance, T[4]])
    Euclidean_distance = sorted(Euclidean_distance)

    nearest_k_neighbour_List = []
    for x in range(K):
        nearest_k_neighbour_List.append(Euclidean_distance[x])
    nearest_k_neighbour_List = np.array(nearest_k_neighbour_List)

    majority = Counter(nearest_k_neighbour_List.flat).most_common(1)

    if majority[0][0] == V[4]:
        correct = correct + 1
test_accuracy = (correct / len(Val_set)) * 100
print("Test Accuracy for K=15 is:", test_accuracy)