# Section D - Program 5
# Sorting Algorithm Comparison
#
# Algorithms tested:
# Bubble Sort, Selection Sort, Insertion Sort,
# Merge Sort, Quick Sort and Heap Sort

import random
import time
import csv

from sorting_basic import bubble_sort, selection_sort, insertion_sort
from merge_quick_heap import merge_sort, quick_sort, heap_sort


# Generate input arrays
def generate_array(n, input_type):
    if input_type == "random":
        return [random.randint(1, 10000) for _ in range(n)]

    elif input_type == "sorted":
        return list(range(n))

    elif input_type == "reverse":
        return list(range(n, 0, -1))


# Dictionary containing all six sorting algorithms
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}


# Four input sizes
sizes = [100, 200, 300, 400]

input_types = ["random", "sorted", "reverse"]

results = []


# Run timing tests
for n in sizes:

    for input_type in input_types:

        original_array = generate_array(n, input_type)

        for algorithm_name, algorithm in algorithms.items():

            test_array = original_array.copy()

            start_time = time.perf_counter()

            try:
                algorithm(test_array)
                end_time = time.perf_counter()

                elapsed_time = end_time - start_time

            except RecursionError:
                elapsed_time = -1

            results.append([
                algorithm_name,
                input_type,
                n,
                elapsed_time
            ])

            print(
                algorithm_name,
                "|",
                input_type,
                "| n =", n,
                "| Time =", elapsed_time
            )


# Save timing results to CSV
with open("timing_results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Algorithm",
        "Input Type",
        "n",
        "Time (seconds)"
    ])

    writer.writerows(results)


# Print final results table
print("\n" + "=" * 70)
print("SORTING ALGORITHM TIMING RESULTS")
print("=" * 70)

print(
    f"{'Algorithm':<20}"
    f"{'Input Type':<15}"
    f"{'n':<8}"
    f"{'Time (seconds)':<20}"
)

print("-" * 70)

for row in results:

    print(
        f"{row[0]:<20}"
        f"{row[1]:<15}"
        f"{row[2]:<8}"
        f"{row[3]:<20.6f}"
    )

print("=" * 70)

print("\nTiming data saved to timing_results.csv")