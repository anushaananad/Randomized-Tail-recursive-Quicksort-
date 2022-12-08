import random
import time
import numpy as np
import partition as p
import dataset as da

def quicksort_naive(A, low, high):
    if (low < high):
        pt = p.lomuto_partition(A, low, high)
        quicksort_naive(A, low, pt-1)
        quicksort_naive(A, pt+1, high)

def call_nqs(A, p, q):
    #print("Input:", A)
    start_time = time.time()
    quicksort_naive(A, p, q)
    end_time = time.time()
    total_time = end_time - start_time
    #print("Output:", A)
    return total_time

def naive_ap(arr, input_size, data_choice):
    if (data_choice == 1):
        print("Quicksort naive on random dataset")
        random_arr = arr.copy()
        total_time = call_nqs(random_arr, 0, input_size-1)

    elif (data_choice == 2):
        print("Quicksort naive on sorted dataset")
        sorted_arr = da.getSortedArray(arr)
        total_time = call_nqs(sorted_arr, 0, input_size-1)

    elif (data_choice == 3):
        print("Quicksort naive on rev-sorted dataset")
        rev_arr = da.getReverseSortedArray(arr)
        total_time = call_nqs(rev_arr, 0, input_size-1)

    elif (data_choice == 4):
        print("Quicksort naive on single valued dataset")
        same_elem = da.getSingleValuedArray(input_size)
        total_time = call_nqs(same_elem, 0, input_size-1)

    elif (data_choice != 5):
        print("Wrong choice!")

    print("Quicksort naive: ","size", input_size, "Time taken:", "%.25f" % (total_time))