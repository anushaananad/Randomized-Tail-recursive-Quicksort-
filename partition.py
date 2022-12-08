import numpy as np

def lomuto_partition_rand_pivot (ar, lo, h):
    random_piv_pt = int(np.random.randint(low=lo, high=h, size=1)) #random
    ar[random_piv_pt], ar[h] = ar[h], ar[random_piv_pt] #swap random with last element
    pivot=ar[h]
    i = lo-1
    for j in range (lo, h):
        if (ar[j] <= pivot):
            i=i+1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i+1], ar[h] = ar[h], ar[i+1]
    return i+1

def lomuto_partition (ar, low, high):
    pivot = ar[high]
    i = low-1
    for j in range (low, high):
        if (ar[j] <= pivot):
            i=i+1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i+1], ar[high] = ar[high], ar[i+1]
    return i+1

def hoare_partition_rand_pivot (ar, lo, hi):
    pivot = int(np.random.randint(low=lo, high=hi, size=1)) #random
    ar[pivot], ar[hi] = ar[hi], ar[pivot] #swap random with last element
    pivot=ar[hi]
    i = lo
    j = hi
    while (True):
        while (ar[i] < pivot):
            i = i+1

        while(ar[j] > pivot):
            j = j-1
        if (i >= j):
            return i
            #print("i=",i)

        ar[i], ar[j] = ar[j], ar[i]
        if (ar[j] == pivot):
            #print("a[j]", ar[j], "pivot", pivot)
            i = i+1
            #print("i++=",i)
        elif (ar[i] == pivot):
            #print("a[i]", ar[i], "pivot", pivot)
            j = j-1
            #print ("j--=",j)