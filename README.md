# IC-2K23-94-PythonLab-TanushkaKamle
## Section A: Concept Check

1. In Python, a 1D array is commonly implemented using a list.
2. Inserting an element at the beginning of a list requires shifting n elements, making it an O(n) operation.
3. Deleting an element from the middle of a list requires shifting all elements after it.
4. Inserting at the end of a list is generally an O(1) operation.
5. Binary search works by checking the middle element repeatedly and requires a sorted array.
6. A sparse matrix stores only non-zero elements along with their row and column positions.
7. A sparse matrix triplet contains row, column, and value.

## Section B: Manual Operations

### 1. 1D Array Operations

Original array:

[10, 20, 30, 40, 50]

Insert 25 at index 2:

[10, 20, 25, 30, 40, 50]

Delete the element at index 0:

[20, 25, 30, 40, 50]

Rotate left by 2 positions:

[40, 50, 20, 25, 30]

### 2. Linear Search

For the array:

[10, 20, 30, 40]

The element 40 is found at index 3.

### 3. Binary Search

For the sorted array:

[2, 5, 8, 10, 15, 20, 25]

Searching for 15:

- low = 0, high = 6, mid = 3 → value = 10
- low = 4, high = 6, mid = 5 → value = 20
- low = 4, high = 4, mid = 4 → value = 15

Therefore, 15 is found at index 4.

### 4. Sparse Matrix Representation

For the matrix:

0 0 5
0 8 0
3 0 0
0 0 0

The triplet representation is:

| Row | Column | Value |
|-----|--------|-------|
| 0 | 2 | 5 |
| 1 | 1 | 8 |
| 2 | 0 | 3 |

Including the header:

(4, 3, 3)

### 5. Full Matrix and Sparse Matrix Storage

A 3 × 4 full matrix stores:

3 × 4 = 12 values

The sparse matrix above contains 3 non-zero values.

Without the header, the sparse representation stores:

3 × 3 = 9 scalar values

Thus, the sparse representation saves space when most matrix elements are zero.

## Section D: Space Analysis

Two 6 × 6 matrices were considered.

### Matrix 1: Approximately 80% zeros

- Total elements = 36
- Non-zero elements = 7
- Zero elements = 29
- Percentage of zeros = 80.56%

Full matrix storage:

36 scalar values

Sparse matrix storage:

7 triplets × 3 values = 21 scalar values

Therefore, the sparse representation uses less space.

### Matrix 2: Fewer than 20% zeros

- Total elements = 36
- Non-zero elements = 30
- Zero elements = 6
- Percentage of zeros = 16.67%

Full matrix storage:

36 scalar values

Sparse matrix storage:

30 triplets × 3 values = 90 scalar values

Therefore, the full matrix representation uses less space for a dense matrix.

## Section E: Conclusion

Through this lab, I implemented and studied:

- 1D array operations
- 2D array operations
- Sparse matrix representation
- Sparse matrix addition
- Matrix addition
- Matrix multiplication
- Matrix transpose
- Matrix determinant

The programs demonstrate how arrays and matrices are stored and manipulated in Python. Sparse matrices are space-efficient when most elements are zero, while full matrix representation is better for dense matrices.


# DSA Lab Assignment

## Section A: Concept Check

### 1. Bubble Sort
Bubble sort works by repeatedly swapping **adjacent** elements if they are in the wrong order.

### 2. Selection Sort
Selection sort repeatedly finds the **minimum (smallest)** element from the unsorted part and places it at the beginning.

### 3. Insertion Sort
Insertion sort builds the sorted portion one element at a time by **inserting** each new element into its correct position.

### 4. Merge Sort
Merge sort follows a **divide-and-conquer** approach: split the array, sort each half, then combine.

### 5. Quick Sort
Quick sort picks a **pivot** and partitions the array around it before recursing.

### 6. Heap Sort
Heap sort relies on a data structure called a **heap**, which is typically implemented using an array.

### 7. Radix Sort
Radix sort processes numbers digit by digit, starting from the **least** significant digit in the standard LSD version.

### 8. Binary Search
Binary search requires the input array to be **sorted** before it can be used.

### 9. Hashing
In hashing, when two different keys map to the same index, this is called a **collision**.

### 10. Collision Handling
Separate chaining resolves collisions by storing multiple values at the same index using a **linked list**, while linear probing resolves them by **searching for the next available slot**.


## Section B: Trace the Logic

### 1. Bubble Sort

Initial array:

`[5, 2, 8, 1, 9]`

One full pass from left to right:

- Compare 5 and 2 → swap  
  `[2, 5, 8, 1, 9]`

- Compare 5 and 8 → no swap

- Compare 8 and 1 → swap  
  `[2, 5, 1, 8, 9]`

- Compare 8 and 9 → no swap

**Array after one full pass:**

`[2, 5, 1, 8, 9]`

---

### 2. Selection Sort

Initial array:

`[5, 2, 8, 1, 9]`

**Step 1:** Find the smallest element (1) and swap it with 5.

`[1, 2, 8, 5, 9]`

**Step 2:** Find the smallest element in the remaining unsorted part (2).

`[1, 2, 8, 5, 9]`

**Step 3:** Find the smallest element in the remaining unsorted part (5) and swap it with 8.

`[1, 2, 5, 8, 9]`

**Step 4:** Find the smallest element in the remaining unsorted part (8).

`[1, 2, 5, 8, 9]`

**Final array:**

`[1, 2, 5, 8, 9]`

---

### 3. Insertion Sort

Initial array:

`[5, 2, 8, 1, 9]`

**Insert 2:**

`[2, 5, 8, 1, 9]`

**Insert 8:**

`[2, 5, 8, 1, 9]`

**Insert 1:**

`[1, 2, 5, 8, 9]`

**Insert 9:**

`[1, 2, 5, 8, 9]`

**Final array:**

`[1, 2, 5, 8, 9]`

---

### 4. Merge Sort — Splitting Step Only

Initial array:

`[8, 3, 5, 4, 7, 6, 1, 2]`

**First split:**

`[8, 3, 5, 4]` and `[7, 6, 1, 2]`

**Second split:**

`[8, 3]`, `[5, 4]`, `[7, 6]`, `[1, 2]`

**Final split:**

`[8]`, `[3]`, `[5]`, `[4]`, `[7]`, `[6]`, `[1]`, `[2]`

---

### 5. Quick Sort — First Partition

Initial array:

`[8, 3, 5, 4, 7, 6, 1, 2]`

Pivot = **2 (last element)**

Using the **Lomuto partition** method:

`[1, 2, 5, 4, 7, 6, 8, 3]`

The pivot `2` is now at:

**Final index = 1**

> Note: The arrangement of elements other than the pivot can vary depending on the partition implementation.

---

### 6. Radix Sort

Initial array:

`[170, 45, 75, 90, 802, 24, 2, 66]`

**After sorting by the ones digit:**

`[170, 90, 802, 2, 24, 45, 75, 66]`

**After sorting by the tens digit:**

`[802, 2, 24, 45, 66, 170, 75, 90]`

---

### 7. Binary Search

Sorted array:

`[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]`

Target = `23`

| Step | Low | High | Mid | Value at Mid |
|------|-----|------|-----|--------------|
| 1 | 0 | 10 | 5 | 23 |

Since `array[5] = 23`, the target is found.

**Result: 23 is found at index 5.**

---

### 8. Hashing — Separate Chaining

Hash table size = `7`

Hash function:

`key % 7`

Keys:

`10, 3, 17, 24, 9`

| Key | Calculation | Initial Index |
|-----|-------------|---------------|
| 10 | 10 % 7 | 3 |
| 3 | 3 % 7 | 3 |
| 17 | 17 % 7 | 3 |
| 24 | 24 % 7 | 3 |
| 9 | 9 % 7 | 2 |

There are collisions at **index 3**.

Using separate chaining:

```text
Index 0 → Empty
Index 1 → Empty
Index 2 → [9]
Index 3 → [10, 3, 17, 24]
Index 4 → Empty
Index 5 → Empty
Index 6 → Empty

### 9. Hashing — Linear Probing

Hash table size = 7

Hash function:

`key % 7`

Keys: `10, 3, 17, 24, 9`

| Key | Calculation | Final Index |
|-----|-------------|-------------|
| 10 | 10 % 7 = 3 | 3 |
| 3 | 3 % 7 = 3 → 4 | 4 |
| 17 | 17 % 7 = 3 → 4 → 5 | 5 |
| 24 | 24 % 7 = 3 → 4 → 5 → 6 | 6 |
| 9 | 9 % 7 = 2 | 2 |

### Final Hash Table

Index 0 → Empty  
Index 1 → Empty  
Index 2 → 9  
Index 3 → 10  
Index 4 → 3  
Index 5 → 17  
Index 6 → 24  

**Collisions:** 3, 17, and 24 initially hash to index 3, so linear probing moves them to the next available positions.