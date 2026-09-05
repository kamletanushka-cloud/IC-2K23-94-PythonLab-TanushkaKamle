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