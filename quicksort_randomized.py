import random
import time
import numpy as np
import partition as p 
import dataset as da

def quicksort_randomized(A, low, high):
    if (low < high):
        pt = p.lomuto_partition_rand_pivot(A, low, high)
        quicksort_randomized(A, low, pt-1)
        quicksort_randomized(A, pt+1, high)

def call_qs(A, p, q):
    #print("Input:", A)
    start_time = time.time()
    quicksort_randomized(A, p, q)
    end_time = time.time()
    total_time = end_time - start_time
    #print("Output:", A)
    return total_time

def randomized_ap(arr, input_size, data_choice):
    if (data_choice == 1):
        print("Quicksort randomized on random dataset")
        random_arr = arr.copy()
        total_time = call_qs(random_arr, 0, input_size-1)

    elif (data_choice == 2):
        print("Quicksort randomized on sorted dataset")
        sorted_arr = da.getSortedArray(arr)
        total_time = call_qs(sorted_arr, 0, input_size-1)

    elif (data_choice == 3):
        print("Quicksort randomized on rev-sorted dataset")
        rev_arr = da.getReverseSortedArray(arr)
        total_time = call_qs(rev_arr, 0, input_size-1)

    elif (data_choice == 4):
        print("Quicksort randomized on single valued dataset")
        same_elem = da.getSingleValuedArray(input_size)
        total_time = call_qs(same_elem, 0, input_size-1)

    else:
        print("Wrong choice!")

    print("Quicksort randomized: ","size", input_size, "Time taken:", "%.25f" % (total_time))