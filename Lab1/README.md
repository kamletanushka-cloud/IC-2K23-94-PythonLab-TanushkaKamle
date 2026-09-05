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