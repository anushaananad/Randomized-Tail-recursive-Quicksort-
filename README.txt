Sorting II. Randomized Quicksort and Tail-Recursive Quicksort

Instruction to run:
1. Run the main.py file.
2. Enter data size you want the algorithm to run on.
3. Choice of algorithms: 
    3.1. Option1: Quicksort Naive - will call the quicksort_naive.py file which contains the naive approach implementation based on the last array element pivot point.
    3.2. Option2: Quicksort Randomised - will call the quicksort_randomized.py file which contains the randomized approach implementation based on
                  lomuto_partition with randomly chosen pivot point.
    3.3. Option3: Tail-recursive Quicksort - will call the quicksort_tailrecursive.py file which contains the tail-recursive approach implementation
                  based on Hoare partition with randomly chosen pivot point.
    3.4. Option4: Change input data size - will allow to change the data size and generates new data for the given size
    3.5. Option5: Exit - exit the program
4. Choice of dataset for a given input size (random data is generated only once unless 3.4 is called, which generates new data):
    4.1 Option1: Random data
    4.2 Option2: Sorted data
    4.3 Option3: Reverse sorted data
    4.4 Option4: Single valued data
5. Go back to step 3 to choose another algorithm or choose option-5 to exit

Files:
1. main.py -> Main calling function for all the algorithms.
2. quicksort_naive.py -> Implementation of naive approach based on the choice of dataset.
3. quicksort_randomized.py -> Implementation of randomized Quicksort approach based on the choice of dataset.
4. quicksort_tailrecursive.py -> Implementation of tail-recursive Quicksort approach based on the choice of dataset.
5. partition.py -> The following partition methods:
    5.1 lomuto-partition -> using the last element as pivot point following lomuto partition approach.
    5.2 lomuto_partition_rand_pivot -> using random element as pivot point following lomuto partition approach.
    5.3 hoare_partition_rand_pivot -> using random element as pivot point following hoare partition approach.
6. dataset.py -> methods to sort, reverse-sort array elements on the provided array data. 
    generates single valued data based on the specified size.
7.  display.py -> display methods to display options on algorithms and dataset.
8. plot.py -> plots the graph for all the 3 algorithms categorised by dataset type. 3 graphs for all the 3 algorithm are generated based on the dataset.
Randomized quick sort -> random pivot. 



Lomuto’s Partition Scheme:
This algorithm works by assuming the pivot element as the last element. 
If any other element is given as a pivot element then swap it first with the last element. 
Now initialize two variables i as low and j also low,  
iterate over the array and increment i when arr[j] <= pivot and swap arr[i] with arr[j] otherwise increment only j. 
After coming out from the loop swap arr[i] with arr[hi]. This i stores the pivot element.


Hoare’s Partition Scheme:

Hoare’s Partition Scheme works by initializing two indexes that start at two ends, 
the two indexes move toward each other until an inversion is 
(A smaller value on the left side and greater value on the right side) found. 
When an inversion is found, two values are swapped and the process is repeated. 


Installations:
Used Visual Studio code to run
Python
python -m pip install matplotlib

