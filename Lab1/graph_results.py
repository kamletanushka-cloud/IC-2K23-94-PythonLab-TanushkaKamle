# Section D - Program 6
# Graphing the Sorting Algorithm Timing Results

import csv
import matplotlib.pyplot as plt


# Read timing data from CSV
data = []

with open("timing_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append({
            "algorithm": row["Algorithm"],
            "input_type": row["Input Type"],
            "n": int(row["n"]),
            "time": float(row["Time (seconds)"])
        })


algorithms = [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
    "Heap Sort"
]


# --------------------------------------------------
# Graph 1: Random Input
# --------------------------------------------------

plt.figure()

for algorithm in algorithms:

    x = []
    y = []

    for row in data:
        if row["algorithm"] == algorithm and row["input_type"] == "random":
            x.append(row["n"])
            y.append(row["time"])

    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms on Random Input")
plt.legend()
plt.grid(True)

plt.savefig("random_comparison.png")
plt.show()


# --------------------------------------------------
# Graph 2: Already Sorted Input
# --------------------------------------------------

plt.figure()

for algorithm in algorithms:

    x = []
    y = []

    for row in data:
        if row["algorithm"] == algorithm and row["input_type"] == "sorted":
            x.append(row["n"])
            y.append(row["time"])

    plt.plot(x, y, marker="o", label=algorithm)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms on Already-Sorted Input")
plt.legend()
plt.grid(True)

plt.savefig("sorted_comparison.png")
plt.show()


print("Graphs saved successfully!")
print("random_comparison.png")
print("sorted_comparison.png")