import random
import time
import numpy as np
import partition as p
import dataset as da

def quicksort_tail_recur(A, low, high):
    while (low < high):
        pt = p.hoare_partition_rand_pivot(A, low, high)
        quicksort_tail_recur(A, low, pt-1)
        low = pt+1

def call_trqs(A, p, q):
    #print("Input:", A)
    start_time = time.time()
    quicksort_tail_recur(A, p, q)
    end_time = time.time()
    total_time = end_time - start_time
    #print("Output:", A)
    return total_time

def tail_recursive_ap(arr, input_size, data_choice):
    if (data_choice == 1):
        print("Quicksort Tail recursive on random dataset")
        random_arr = arr.copy()
        total_time = call_trqs(random_arr, 0, input_size-1)

    elif (data_choice == 2):
        print("Quicksort Tail recursive on sorted dataset")
        sorted_arr = da.getSortedArray(arr)
        total_time = call_trqs(sorted_arr, 0, input_size-1)

    elif (data_choice == 3):
        print("Quicksort Tail recursive on rev-sorted dataset")
        rev_arr = da.getReverseSortedArray(arr)
        total_time = call_trqs(rev_arr, 0, input_size-1)

    elif (data_choice == 4):
        print("Quicksort Tail recursive on single valued dataset")
        same_elem = da.getSingleValuedArray(input_size)
        total_time = call_trqs(same_elem, 0, input_size-1)

    else:
        print("Wrong choice!")

    print("Quicksort Tail recursive: ","size", input_size, "Time taken:", "%.25f" % (total_time))