# coding: utf8


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def prixEstime(kilometrage, teta0 = 0, teta1 = 0):
    return teta0 + ( teta1 * kilometrage)


def computeTeta0():
    ## m doit etre la taille du csv
    m = 10
    # ratioApprentissage * 1 



def main():
    data = pd.read_csv("data.csv")
    # data.head()
    data.plot(kind='scatter', x='km', y='price', figsize=(12,8))

    print(data)
    # data.describe()
    # plt.figure()

    # slope 
    m = 1
    # intercept
    b = 2

    x = data.km
    y = data.price
    plt.scatter(x, y)
    plt.plot(x, m * x + b)

    plt.show()







if __name__ == '__main__':
    main()
    