from ctypes import Array
import numpy as np
import quicksort_naive as qs_naive
import quicksort_randomized as qs_rand
import quicksort_tailrecursive as qs_tailrec
import time
import array 
import display as dis
import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
input_size = int(input("Enter the input size:"))
arr = np.random.randint(low=1, high=100000, size=input_size)

algo_choice = 0

while (algo_choice != 5):
    dis.display_algorithm_choice()
    algo_choice = int(input("Enter your choice of algorithm:"))

    if (algo_choice == 1):
        dis.display_dataset_choice()
        data_choice = int(input("Enter your choice for dataset:"))
        qs_naive.naive_ap(arr, input_size, data_choice)

    elif (algo_choice == 2):
        dis.display_dataset_choice()
        data_choice = int(input("Enter your choice for dataset:"))
        qs_rand.randomized_ap(arr, input_size, data_choice)

    elif (algo_choice == 3):
        dis.display_dataset_choice()
        data_choice = int(input("Enter your choice for dataset:"))
        qs_tailrec.tail_recursive_ap(arr, input_size, data_choice)

    elif (algo_choice == 4):
        input_size = int(input("Enter the input size:"))
        arr = np.random.randint(low=1, high=100000, size=input_size)
    
    elif (data_choice != 5):
        print("Wrong choice!")
