# Section E - Program 7
# Student Record Manager

import time

from sorting_basic import bubble_sort, selection_sort, insertion_sort
from merge_quick_heap import merge_sort, quick_sort, heap_sort


# Student records
students = [
    {"roll": 105, "name": "Riya", "marks": 78},
    {"roll": 102, "name": "Aarav", "marks": 91},
    {"roll": 108, "name": "Neha", "marks": 85},
    {"roll": 101, "name": "Kabir", "marks": 67},
    {"roll": 104, "name": "Anaya", "marks": 95},
]


# Sorting algorithms
sorting_algorithms = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Insertion Sort", insertion_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
    "6": ("Heap Sort", heap_sort)
}


# Sort student records
def sort_students(records, key):
    # Convert records into sortable tuples
    data = [(student[key], student) for student in records]

    # Sorting functions work on the first value
    values = [item[0] for item in data]

    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")

    choice = input("Enter your choice: ")

    if choice not in sorting_algorithms:
        print("Invalid choice.")
        return records

    algorithm_name, algorithm = sorting_algorithms[choice]

    sorted_values = algorithm(values)

    sorted_records = []

    for value in sorted_values:
        for item in data:
            if item[0] == value and item[1] not in sorted_records:
                sorted_records.append(item[1])
                break

    print("\nSorted using:", algorithm_name)

    return sorted_records


# Display student records
def display_students(records):
    print("\nRoll No.   Name       Marks")
    print("---------------------------")

    for student in records:
        print(
            student["roll"],
            "       ",
            student["name"],
            "     ",
            student["marks"]
        )


# Binary search by roll number
def binary_search_roll(records, target):
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2

        if records[mid]["roll"] == target:
            return mid

        elif records[mid]["roll"] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Compare sorting algorithm performance
def compare_algorithms(records, key):

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]

    results = []

    values = [student[key] for student in records]

    print("\nPerformance Comparison")
    print("----------------------")

    for name, algorithm in algorithms:

        start = time.perf_counter()

        algorithm(values.copy())

        end = time.perf_counter()

        elapsed = end - start

        results.append((name, elapsed))

        print(name, ":", elapsed, "seconds")

    fastest = min(results, key=lambda x: x[1])
    slowest = max(results, key=lambda x: x[1])

    print("\nFastest Algorithm:", fastest[0])
    print("Time:", fastest[1], "seconds")

    print("\nSlowest Algorithm:", slowest[0])
    print("Time:", slowest[1], "seconds")

    difference = slowest[1] - fastest[1]

    print("\nDifference between slowest and fastest:",
          difference, "seconds")


# Main program
def main():

    records = students.copy()

    while True:

        print("\n===== Student Record Manager =====")
        print("1. Display Students")
        print("2. Sort Students")
        print("3. Search Student by Roll Number")
        print("4. Compare Sorting Algorithms")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            display_students(records)

        elif choice == "2":

            print("\nSort by:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")

            sort_choice = input("Enter your choice: ")

            if sort_choice == "1":
                records = sort_students(records, "roll")

            elif sort_choice == "2":
                records = sort_students(records, "name")

            elif sort_choice == "3":
                records = sort_students(records, "marks")

            else:
                print("Invalid choice.")

            display_students(records)

        elif choice == "3":

            # Binary search requires records sorted by roll number
            records = sorted(records, key=lambda x: x["roll"])

            target = int(input("Enter roll number to search: "))

            index = binary_search_roll(records, target)

            if index != -1:
                print("\nStudent Found:")
                print(records[index])
            else:
                print("\nStudent not found.")

        elif choice == "4":

            print("\nCompare sorting by:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")

            compare_choice = input("Enter your choice: ")

            if compare_choice == "1":
                compare_algorithms(records, "roll")

            elif compare_choice == "2":
                compare_algorithms(records, "name")

            elif compare_choice == "3":
                compare_algorithms(records, "marks")

            else:
                print("Invalid choice.")

        elif choice == "5":

            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()