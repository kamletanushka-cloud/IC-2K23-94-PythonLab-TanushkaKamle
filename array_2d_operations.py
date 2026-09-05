# This program performs insertion, deletion, searching, and
# 90-degree clockwise rotation operations on a 2D array.

def display_matrix(matrix):
    """Display the matrix row by row."""
    print("\nCurrent 2D Array:")
    if len(matrix) == 0:
        print("[]")
    else:
        for row in matrix:
            print(row)


def get_matrix():
    """Take a 2D array as input."""
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows < 0 or cols < 0:
            print("Dimensions cannot be negative.")
            return None

        matrix = []

        for i in range(rows):
            row = []
            print(f"Enter {cols} elements for row {i}:")
            for j in range(cols):
                value = int(input(f"Element [{i}][{j}]: "))
                row.append(value)
            matrix.append(row)

        return matrix

    except ValueError:
        print("Please enter valid integer values.")
        return None


def insert_row(matrix):
    """Insert a new row at a valid position."""
    if len(matrix) == 0:
        print("Matrix is empty. Cannot determine column count.")
        return

    try:
        index = int(input("Enter row position to insert: "))

        if index < 0 or index > len(matrix):
            print("Invalid row position!")
            return

        cols = len(matrix[0])
        new_row = []

        print(f"Enter {cols} elements for the new row:")
        for j in range(cols):
            value = int(input(f"Element {j}: "))
            new_row.append(value)

        matrix.insert(index, new_row)

        print("Row inserted successfully.")
        display_matrix(matrix)

    except ValueError:
        print("Please enter valid integer values.")


def delete_row(matrix):
    """Delete a row at a valid position."""
    if len(matrix) == 0:
        print("Matrix is empty. Nothing to delete.")
        return

    try:
        index = int(input("Enter row position to delete: "))

        if index < 0 or index >= len(matrix):
            print("Invalid row position!")
            return

        deleted = matrix.pop(index)

        print("Deleted row:", deleted)
        display_matrix(matrix)

    except ValueError:
        print("Please enter a valid integer.")


def search_value(matrix):
    """Search for a value across the entire matrix."""
    if len(matrix) == 0:
        print("Matrix is empty.")
        return

    try:
        value = int(input("Enter value to search: "))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == value:
                    print(f"Value found at row {i}, column {j}")
                    return

        print("Value not found.")

    except ValueError:
        print("Please enter a valid integer.")


def rotate_clockwise(matrix):
    """Rotate the entire matrix 90 degrees clockwise."""
    if len(matrix) == 0:
        print("Matrix is empty.")
        return

    if len(matrix[0]) == 0:
        print("Matrix has no columns.")
        return

    matrix[:] = [list(row) for row in zip(*matrix[::-1])]

    print("Matrix rotated 90 degrees clockwise.")
    display_matrix(matrix)


def main():
    """Main menu-driven program."""

    matrix = get_matrix()

    if matrix is None:
        return

    display_matrix(matrix)

    while True:
        print("\n--- 2D ARRAY MENU ---")
        print("1. Insert new row")
        print("2. Delete row")
        print("3. Search for a value")
        print("4. Rotate 90 degrees clockwise")
        print("5. Display matrix")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_row(matrix)

        elif choice == "2":
            delete_row(matrix)

        elif choice == "3":
            search_value(matrix)

        elif choice == "4":
            rotate_clockwise(matrix)

        elif choice == "5":
            display_matrix(matrix)

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()