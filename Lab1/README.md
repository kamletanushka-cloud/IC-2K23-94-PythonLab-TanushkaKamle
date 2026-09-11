# Python Lab 1

Name: Tanushka Kamle
Roll No: IC-2K23-94

## 1. 1D Array Operations

### Aim
To perform insertion, deletion, linear search, and left/right rotation on a 1D array.

### Logic
The program uses a Python list and functions for each operation. It validates indices before insertion or deletion and displays the array after every operation.

### Sample Input / Output
Input: [10, 20, 30, 40, 50]
Insert 25 at index 2
Output: [10, 20, 25, 30, 40, 50]

Delete element at index 0
Output: [20, 25, 30, 40, 50]

Rotate left by 2
Output: [40, 50, 20, 25, 30]

Boundary case: Searching for 100
Output: Value not found.

## 2. 2D Array Operations

### Aim
To perform row insertion, row deletion, searching, and 90-degree clockwise rotation on a 2D array.

### Logic
The program uses a list of lists. It validates row positions and dimensions before performing operations and displays the matrix row by row.

### Sample Input / Output
Input:
[1, 2, 3]
[4, 5, 6]

Insert row [7, 8, 9] at position 1

Output:
[1, 2, 3]
[7, 8, 9]
[4, 5, 6]

Rotate 90 degrees clockwise

Output:
[4, 7, 1]
[5, 8, 2]
[6, 9, 3]

Boundary case: Invalid row position
Output: Invalid row position!

## 3. Sparse Matrix Representation

### Aim
To convert a full matrix into sparse triple form, reconstruct it, and add two sparse matrices.

### Logic
Only non-zero elements are stored as (row, column, value). Sparse addition is performed by combining entries with the same row and column without converting the input matrices back to full form.

### Sample Input / Output
Input matrix:
[0, 0, 5]
[0, 8, 0]
[3, 0, 0]

Sparse representation:
(0, 2, 5)
(1, 1, 8)
(2, 0, 3)

Reconstructed matrix:
[0, 0, 5]
[0, 8, 0]
[3, 0, 0]

### Section D Analysis
For an m x n matrix with k non-zero elements:
- Full representation stores m x n values.
- Sparse representation stores 3k values, excluding the header.

A 6 x 6 matrix with 80% zeros stores approximately 7 non-zero values. Full: 36 values. Sparse: 21 values. Sparse representation saves space.

A 6 x 6 matrix with fewer than 20% zeros stores approximately 30 non-zero values. Full: 36 values. Sparse: 90 values. Full representation saves space.

Sparse representation stops saving space when approximately 33% of the elements are non-zero.

Real-world example: Graph adjacency matrices are naturally sparse because most vertices are not directly connected to every other vertex.

## 4. Matrix Calculator

### Aim
To perform matrix addition, multiplication, transpose, and determinant operations using a menu-driven program.

### Logic
The program validates matrix dimensions before addition and multiplication. It checks that the matrix is square before calculating its determinant.

### Sample Input / Output
Matrix A:
[1, 2]
[3, 4]

Matrix B:
[5, 6]
[7, 8]

Addition:
[6, 8]
[10, 12]

Multiplication:
[19, 22]
[43, 50]

Transpose:
[1, 3]
[2, 4]

Determinant:
-2

Boundary case: Incompatible dimensions
Output: Matrix dimensions are not compatible.

# DSA Lab Assignment

## Section A: Concept Check

### 1. Bubble Sort
Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order.

### 2. Selection Sort
Selection sort repeatedly finds the minimum (smallest) element from the unsorted part and places it at the beginning.

### 3. Insertion Sort
Insertion sort builds the sorted portion one element at a time by inserting each new element into its correct position.

### 4. Merge Sort
Merge sort follows a divide-and-conquer approach: split the array, sort each half, then combine.

### 5. Quick Sort
Quick sort picks a pivot and partitions the array around it before recursing.

### 6. Heap Sort
Heap sort relies on a data structure called a heap, which is typically implemented using an array.

### 7. Radix Sort
Radix sort processes numbers digit by digit, starting from the least significant digit in the standard LSD version.

### 8. Binary Search
Binary search requires the input array to be sorted before it can be used.

### 9. Hashing
In hashing, when two different keys map to the same index, this is called a collision.

### 10. Collision Handling
Separate chaining resolves collisions by storing multiple values at the same index using a linked list, while linear probing resolves them by searching for the next available slot.


# Section B: Trace the Logic

## 1. Bubble Sort

Initial array:

[5, 2, 8, 1, 9]

One full pass:

Compare 5 and 2 → swap

[2, 5, 8, 1, 9]

Compare 5 and 8 → no swap

Compare 8 and 1 → swap

[2, 5, 1, 8, 9]

Compare 8 and 9 → no swap

Array after one full pass:

[2, 5, 1, 8, 9]


## 2. Selection Sort

Initial array:

[5, 2, 8, 1, 9]

Step 1: Smallest element is 1.

[1, 2, 8, 5, 9]

Step 2: Smallest element in the remaining unsorted part is 2.

[1, 2, 8, 5, 9]

Step 3: Smallest element is 5.

[1, 2, 5, 8, 9]

Step 4: Smallest element is 8.

[1, 2, 5, 8, 9]

Final array:

[1, 2, 5, 8, 9]


## 3. Insertion Sort

Initial array:

[5, 2, 8, 1, 9]

Insert 2:

[2, 5, 8, 1, 9]

Insert 8:

[2, 5, 8, 1, 9]

Insert 1:

[1, 2, 5, 8, 9]

Insert 9:

[1, 2, 5, 8, 9]

Final array:

[1, 2, 5, 8, 9]


## 4. Merge Sort - Splitting Step Only

Initial array:

[8, 3, 5, 4, 7, 6, 1, 2]

First split:

[8, 3, 5, 4]    [7, 6, 1, 2]

Second split:

[8, 3]    [5, 4]    [7, 6]    [1, 2]

Final split:

[8] [3] [5] [4] [7] [6] [1] [2]


## 5. Quick Sort - First Partition

Initial array:

[8, 3, 5, 4, 7, 6, 1, 2]

Pivot = 2 (last element)

Using the Lomuto partition method:

[1, 2, 5, 4, 7, 6, 8, 3]

Pivot final index = 1


## 6. Radix Sort

Initial array:

[170, 45, 75, 90, 802, 24, 2, 66]

After sorting by ones digit:

[170, 90, 802, 2, 24, 45, 75, 66]

After sorting by tens digit:

[802, 2, 24, 45, 66, 170, 75, 90]


## 7. Binary Search

Sorted array:

[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

Target = 23

Step 1:

Low = 0
High = 10
Mid = 5

Array[5] = 23

Therefore, 23 is found at index 5.


## 8. Hashing - Separate Chaining

Hash table size = 7

Hash function:

key % 7

Keys:

10, 3, 17, 24, 9

10 % 7 = 3 → index 3

3 % 7 = 3 → collision at index 3

17 % 7 = 3 → collision at index 3

24 % 7 = 3 → collision at index 3

9 % 7 = 2 → index 2

Final hash table:

Index 0 → Empty
Index 1 → Empty
Index 2 → [9]
Index 3 → [10, 3, 17, 24]
Index 4 → Empty
Index 5 → Empty
Index 6 → Empty


## 9. Hashing - Linear Probing

Hash table size = 7

Hash function:

key % 7

Keys:

10, 3, 17, 24, 9

10 % 7 = 3 → 10 goes to index 3

3 % 7 = 3 → index 3 occupied → 3 goes to index 4

17 % 7 = 3 → indexes 3 and 4 occupied → 17 goes to index 5

24 % 7 = 3 → indexes 3, 4 and 5 occupied → 24 goes to index 6

9 % 7 = 2 → 9 goes to index 2

Final hash table:

Index 0 → Empty
Index 1 → Empty
Index 2 → 9
Index 3 → 10
Index 4 → 3
Index 5 → 17
Index 6 → 24

Collisions occur because 3, 17 and 24 initially hash to index 3. Linear probing checks the next available index.


# Section C: Programs to Write

## 1. Bubble Sort, Selection Sort and Insertion Sort

File: sorting_basic.py

Aim:
To implement Bubble Sort, Selection Sort and Insertion Sort as separate functions and display the sorting process.

Logic:
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. Selection Sort selects the smallest element from the unsorted part. Insertion Sort inserts each element into its correct position in the sorted part.

Sample Input:

[5, 2, 8, 1, 9]

Sample Output:

Bubble Sort → [1, 2, 5, 8, 9]

Selection Sort → [1, 2, 5, 8, 9]

Insertion Sort → [1, 2, 5, 8, 9]


## 2. Merge Sort, Quick Sort and Heap Sort

File: merge_quick_heap.py

Aim:
To implement Merge Sort, Quick Sort and Heap Sort.

Logic:
Merge Sort divides the array into smaller parts and merges them after sorting. Quick Sort partitions the array around a pivot. Heap Sort uses a heap structure to repeatedly select the largest element.

Quick Sort Pivot:
Last element using Lomuto partition.

Sample Input:

[8, 3, 5, 4, 7, 6, 1, 2]

Sample Output:

[1, 2, 3, 4, 5, 6, 7, 8]


## 3. Radix Sort

File: radix_sort.py

Aim:
To implement Radix Sort using the Least Significant Digit (LSD) approach.

Logic:
The algorithm processes numbers digit by digit starting from the ones digit. Counting Sort is used as a helper function for each digit position.

Sample Input:

[170, 45, 75, 90, 802, 24, 2, 66]

Sample Output:

[2, 24, 45, 66, 75, 90, 170, 802]


## 4. Binary Search

File: binary_search.py

Aim:
To implement iterative Binary Search on a sorted array.

Logic:
Binary Search repeatedly checks the middle element and eliminates half of the remaining search space based on whether the target is smaller or larger.

Sample Input:

Array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

Target 1 = 23

Target 2 = 50

Sample Output:

23 found at index 5

50 not found


# Section D: Empirical Timing Analysis

## 5. Sorting Algorithm Comparison

File: timing_analysis.py

Aim:
To compare the execution time of six sorting algorithms on random, sorted and reverse-sorted arrays.

Algorithms tested:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort

Input sizes used:

100, 200, 300, 400

Input types:

1. Random
2. Already Sorted
3. Reverse Sorted

The program records the execution time of each algorithm and saves the results in timing_results.csv.

Timing Results:

The actual timing results will be added after running the program.

| Algorithm | Input Type | n | Time (seconds) |
|-----------|------------|---|----------------|
| Bubble Sort | Random | | |
| Bubble Sort | Sorted | | |
| Bubble Sort | Reverse | | |
| Selection Sort | Random | | |
| Selection Sort | Sorted | | |
| Selection Sort | Reverse | | |
| Insertion Sort | Random | | |
| Insertion Sort | Sorted | | |
| Insertion Sort | Reverse | | |
| Merge Sort | Random | | |
| Merge Sort | Sorted | | |
| Merge Sort | Reverse | | |
| Quick Sort | Random | | |
| Quick Sort | Sorted | | |
| Quick Sort | Reverse | | |
| Heap Sort | Random | | |
| Heap Sort | Sorted | | |
| Heap Sort | Reverse | | |


## 6. Graphing the Results

File: graph_results.py

Aim:
To graphically compare the execution time of the six sorting algorithms.

Logic:
The program reads timing_results.csv and creates graphs using Matplotlib. One graph compares random input and another compares already-sorted input.

Generated files:

random_comparison.png

sorted_comparison.png

timing_results.csv

The actual graphs and timing data will be added after running the programs.


# Section E: Applications

## 7. Student Record Manager

File: student_record_manager.py

Aim:
To create a student record management system that can sort and search student records.

Student records contain:

Roll Number
Name
Marks

The program allows sorting by:

1. Roll Number
2. Name
3. Marks

The user can select:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort

Binary Search is used to search for a student by roll number after sorting the records by roll number.

The program also compares the execution time of all six sorting algorithms and reports the fastest and slowest algorithms.


## 8. Search Engine Simulator

File: search_engine_simulator.py

Aim:
To create a simplified search engine using Binary Search and two hash table collision-handling techniques.

Logic:
The program stores more than 30 words with mock document IDs. It searches for a word using Binary Search, Separate Chaining and Linear Probing and reports the number of comparisons or probes.

Search methods:

1. Binary Search
2. Hashing with Separate Chaining
3. Hashing with Linear Probing

The program reports whether the word was found and the number of steps required by each method.


# Section F: Analysis

## 1. Timing Results on Different Input Types

Bubble Sort, Selection Sort and Insertion Sort are affected differently by the input arrangement. Bubble Sort and Insertion Sort can perform better on already-sorted input because fewer swaps or movements are required. Selection Sort performs almost the same amount of work regardless of whether the input is random, sorted or reverse-sorted because it still searches for the minimum element in the unsorted portion.

Merge Sort generally performs consistently because it always divides the array and performs merging regardless of the original order.

Quick Sort can perform much worse on already-sorted or reverse-sorted input when the last element is selected as the pivot. This can produce highly unbalanced partitions.

Heap Sort generally stays close to the same performance for different input arrangements because it builds and processes a heap regardless of the initial ordering.


## 2. Bubble Sort, Selection Sort and Insertion Sort on Reverse-Sorted Input

On reverse-sorted input, all three algorithms can require quadratic time.

Insertion Sort usually performs many shifts because every new element has to move toward the beginning.

Bubble Sort performs many swaps because adjacent elements are repeatedly exchanged.

Selection Sort still performs its regular comparisons but performs relatively few swaps.

The expected time complexity for all three in the worst case is O(n²).


## 3. Merge Sort vs Quick Sort

Both Merge Sort and Quick Sort use divide-and-conquer.

The difference is the way they divide the array.

In our Quick Sort implementation, the last element is always selected as the pivot. For an already-sorted or reverse-sorted array, this can result in very unbalanced partitions.

This can make Quick Sort approach O(n²) time.

Merge Sort divides the array into two roughly equal parts, giving it O(n log n) time consistently.


## 4. Radix Sort

Radix Sort does not compare elements directly. It processes numbers digit by digit.

For non-negative integers with a reasonable number of digits, Radix Sort can be very efficient.

However, it is mainly suitable for integer-like data that can be processed digit by digit. It is not directly suitable for general data such as names or arbitrary objects.

A very large range of integer values can also require processing many digit positions.


## 5. Binary Search vs Hashing

Binary Search has a theoretical time complexity of O(log n), while hashing has an average lookup complexity of O(1).

Therefore, hash table lookup generally requires fewer steps on average.

However, collisions can increase the number of comparisons or probes.

The actual number of steps depends on the dataset, hash function and collision-handling method.


## 6. Separate Chaining vs Linear Probing

For our particular dataset, the better method depends on the number of collisions and how the table is filled.

Separate Chaining can handle multiple collisions at one index by storing multiple elements in the same chain.

Linear Probing searches for another empty position in the table.

If the hash table becomes very full, such as 90 percent occupied, Linear Probing can become inefficient because many consecutive positions may be occupied.

Separate Chaining generally handles high load factors better because the chains can continue to hold multiple elements.


# Section G: Documentation

## Program 1 - Bubble Sort, Selection Sort and Insertion Sort

Aim:
To implement and demonstrate three basic sorting algorithms.

Logic:
Each algorithm sorts the input using a different technique. The program displays the array after each pass or step.

Sample Input:

[5, 2, 8, 1, 9]

Sample Output:

[1, 2, 5, 8, 9]


## Program 2 - Merge Sort, Quick Sort and Heap Sort

Aim:
To implement three advanced sorting algorithms.

Logic:
Merge Sort uses divide-and-conquer, Quick Sort uses partitioning around a pivot, and Heap Sort uses a heap.

Sample Input:

[8, 3, 5, 4, 7, 6, 1, 2]

Sample Output:

[1, 2, 3, 4, 5, 6, 7, 8]


## Program 3 - Radix Sort

Aim:
To implement LSD Radix Sort for non-negative integers.

Logic:
Numbers are sorted according to each digit position using Counting Sort.

Sample Input:

[170, 45, 75, 90, 802, 24, 2, 66]

Sample Output:

[2, 24, 45, 66, 75, 90, 170, 802]


## Program 4 - Binary Search

Aim:
To search for an element efficiently in a sorted array.

Logic:
The search repeatedly checks the middle element and eliminates half of the search space.

Sample Input:

Target = 23

Sample Output:

23 found at index 5.


## Program 5 - Sorting Algorithm Comparison

Aim:
To compare the execution times of six sorting algorithms using different input types and sizes.

Logic:
The program generates random, sorted and reverse-sorted arrays and measures the execution time of each algorithm.

Output:

Timing table will be added after execution.

CSV file:

timing_results.csv


## Program 6 - Graphing Results

Aim:
To visualize the sorting algorithm timing results.

Logic:
The program reads the CSV timing data and creates two graphs using Matplotlib.

Output files:

random_comparison.png

sorted_comparison.png


## Program 7 - Student Record Manager

Aim:
To manage, sort and search student records.

Logic:
Student records can be sorted by roll number, name or marks using the selected sorting algorithm. Binary Search is used to find a student by roll number.

Performance Report:

To be added after execution of the program.


## Program 8 - Search Engine Simulator

Aim:
To compare Binary Search, Separate Chaining and Linear Probing for word lookup.

Logic:
The program searches the same word using all three methods and records the comparisons or probes required.

Search Step Counts:

To be added after execution of the program.


## Section F Analysis

The complete analysis is provided in Section F above.