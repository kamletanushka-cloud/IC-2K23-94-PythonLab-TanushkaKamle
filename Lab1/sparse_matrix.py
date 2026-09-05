# This program converts a full matrix into sparse triple form,
# reconstructs the matrix, and adds two sparse matrices.

def display_matrix(matrix):
    """Display a matrix row by row."""
    for row in matrix:
        print(row)


def convert_to_sparse(matrix):
    """Convert a full matrix into sparse triple representation."""
    rows = len(matrix)
    cols = len(matrix[0])
    sparse = [(rows, cols, 0)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append((i, j, matrix[i][j]))

    sparse[0] = (rows, cols, len(sparse) - 1)
    return sparse


def reconstruct_matrix(sparse):
    """Reconstruct a full matrix from sparse triples."""
    rows, cols, non_zero = sparse[0]
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for row, col, value in sparse[1:]:
        matrix[row][col] = value

    return matrix


def add_sparse_matrices(s1, s2):
    """Add two matrices directly in sparse form."""
    if s1[0][0] != s2[0][0] or s1[0][1] != s2[0][1]:
        print("Error: Matrix dimensions must match.")
        return None

    rows, cols, _ = s1[0]
    result = {}

    for row, col, value in s1[1:]:
        result[(row, col)] = value

    for row, col, value in s2[1:]:
        result[(row, col)] = result.get((row, col), 0) + value

    sparse_result = [(rows, cols, 0)]

    for (row, col), value in sorted(result.items()):
        if value != 0:
            sparse_result.append((row, col, value))

    sparse_result[0] = (rows, cols, len(sparse_result) - 1)
    return sparse_result


def get_matrix():
    """Take a matrix as input."""
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            print("Dimensions must be positive.")
            return None

        matrix = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = int(input(f"Element [{i}][{j}]: "))
                row.append(value)
            matrix.append(row)

        return matrix

    except ValueError:
        print("Please enter valid integers.")
        return None


def display_sparse(sparse):
    """Display sparse triples."""
    print("\nSparse Triple Representation:")
    for triple in sparse:
        print(triple)


def main():
    print("--- SPARSE MATRIX PROGRAM ---")

    print("\nEnter first matrix:")
    matrix1 = get_matrix()

    if matrix1 is None:
        return

    print("\nEnter second matrix:")
    matrix2 = get_matrix()

    if matrix2 is None:
        return

    sparse1 = convert_to_sparse(matrix1)
    sparse2 = convert_to_sparse(matrix2)

    display_sparse(sparse1)
    print("\nReconstructed First Matrix:")
    display_matrix(reconstruct_matrix(sparse1))

    display_sparse(sparse2)
    print("\nReconstructed Second Matrix:")
    display_matrix(reconstruct_matrix(sparse2))

    result = add_sparse_matrices(sparse1, sparse2)

    if result is not None:
        display_sparse(result)

        print("\nReconstructed Result Matrix:")
        display_matrix(reconstruct_matrix(result))


if __name__ == "__main__":
    main()