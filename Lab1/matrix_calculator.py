# This program performs matrix addition, multiplication,
# transpose, and determinant calculation using a menu.

def display_matrix(matrix):
    """Display a matrix row by row."""
    for row in matrix:
        print(row)


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


def add_matrices(a, b):
    """Add two matrices if their dimensions match."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Error: Matrix dimensions must match.")
        return None

    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def multiply_matrices(a, b):
    """Multiply two matrices if dimensions are compatible."""
    if len(a[0]) != len(b):
        print("Error: Columns of first matrix must equal rows of second.")
        return None

    result = [
        [0 for _ in range(len(b[0]))]
        for _ in range(len(a))
    ]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transpose_matrix(matrix):
    """Return the transpose of a matrix."""
    return [list(row) for row in zip(*matrix)]


def determinant(matrix):
    """Find determinant of a 2x2 or 3x3 matrix."""
    n = len(matrix)

    if n != len(matrix[0]):
        print("Error: Matrix must be square.")
        return None

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if n == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]

        return (
            a * (e * i - f * h)
            - b * (d * i - f * g)
            + c * (d * h - e * g)
        )

    print("Determinant is supported only for 1x1, 2x2, and 3x3 matrices.")
    return None


def main():
    while True:
        print("\n--- MATRIX CALCULATOR ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find determinant")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter first matrix:")
            a = get_matrix()

            if a is None:
                continue

            print("\nEnter second matrix:")
            b = get_matrix()

            if b is None:
                continue

            result = add_matrices(a, b)

            if result is not None:
                print("\nResult:")
                display_matrix(result)

        elif choice == "2":
            print("\nEnter first matrix:")
            a = get_matrix()

            if a is None:
                continue

            print("\nEnter second matrix:")
            b = get_matrix()

            if b is None:
                continue

            result = multiply_matrices(a, b)

            if result is not None:
                print("\nResult:")
                display_matrix(result)

        elif choice == "3":
            print("\nEnter matrix:")
            matrix = get_matrix()

            if matrix is not None:
                print("\nTranspose:")
                display_matrix(transpose_matrix(matrix))

        elif choice == "4":
            print("\nEnter matrix:")
            matrix = get_matrix()

            if matrix is not None:
                result = determinant(matrix)

                if result is not None:
                    print("Determinant:", result)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()