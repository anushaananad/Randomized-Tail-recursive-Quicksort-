import numpy as np

def getSortedArray(arr):
    return (sorted(arr))

def getReverseSortedArray(arr):
    return (sorted(arr, reverse=True))

def getSingleValuedArray(size):
    return ([np.random.randint(1, 1000000)] * size)