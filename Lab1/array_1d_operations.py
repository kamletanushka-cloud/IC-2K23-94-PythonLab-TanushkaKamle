# This program performs insertion, deletion, searching, and rotation
# operations on a 1D array using a Python list.

def display_array(arr):
    """Display the current array."""
    print("Current array:", arr)


def insert_value(arr):
    """Insert a value at a valid index."""
    try:
        index = int(input("Enter index: "))

        if index < 0 or index > len(arr):
            print("Invalid index! Valid insertion index is 0 to", len(arr))
            return

        value = int(input("Enter value: "))
        arr.insert(index, value)

        print("Value inserted successfully.")
        display_array(arr)

    except ValueError:
        print("Please enter a valid integer.")


def delete_value(arr):
    """Delete a value at a valid index."""
    if len(arr) == 0:
        print("Array is empty. Nothing to delete.")
        return

    try:
        index = int(input("Enter index to delete: "))

        if index < 0 or index >= len(arr):
            print("Invalid index! Valid deletion index is 0 to", len(arr) - 1)
            return

        deleted = arr.pop(index)

        print("Deleted value:", deleted)
        display_array(arr)

    except ValueError:
        print("Please enter a valid integer.")


def linear_search(arr):
    """Search for a value using linear search."""
    if len(arr) == 0:
        print("Array is empty.")
        return

    try:
        value = int(input("Enter value to search: "))

        for i in range(len(arr)):
            if arr[i] == value:
                print("Value found at index:", i)
                return

        print("Value not found.")

    except ValueError:
        print("Please enter a valid integer.")


def rotate_left(arr):
    """Rotate the array left by k positions."""
    if len(arr) == 0:
        print("Array is empty.")
        return

    try:
        k = int(input("Enter number of positions: "))

        if k < 0:
            print("Number of positions cannot be negative.")
            return

        k = k % len(arr)
        arr[:] = arr[k:] + arr[:k]

        print("Array rotated left.")
        display_array(arr)

    except ValueError:
        print("Please enter a valid integer.")


def rotate_right(arr):
    """Rotate the array right by k positions."""
    if len(arr) == 0:
        print("Array is empty.")
        return

    try:
        k = int(input("Enter number of positions: "))

        if k < 0:
            print("Number of positions cannot be negative.")
            return

        k = k % len(arr)

        if k == 0:
            print("Array rotated right.")
            display_array(arr)
            return

        arr[:] = arr[-k:] + arr[:-k]

        print("Array rotated right.")
        display_array(arr)

    except ValueError:
        print("Please enter a valid integer.")


def main():
    """Main menu-driven program."""

    try:
        n = int(input("Enter number of elements: "))

        if n < 0:
            print("Number of elements cannot be negative.")
            return

        arr = []

        if n > 0:
            print("Enter", n, "elements:")
            for i in range(n):
                value = int(input(f"Element {i}: "))
                arr.append(value)

        display_array(arr)

        while True:
            print("\n--- 1D ARRAY MENU ---")
            print("1. Insert value")
            print("2. Delete value")
            print("3. Linear search")
            print("4. Rotate left")
            print("5. Rotate right")
            print("6. Display array")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                insert_value(arr)

            elif choice == "2":
                delete_value(arr)

            elif choice == "3":
                linear_search(arr)

            elif choice == "4":
                rotate_left(arr)

            elif choice == "5":
                rotate_right(arr)

            elif choice == "6":
                display_array(arr)

            elif choice == "7":
                print("Program ended.")
                break

            else:
                print("Invalid choice! Please try again.")

    except ValueError:
        print("Please enter valid integer values.")


if __name__ == "__main__":
    main()