# Section C - Program 1
# Bubble Sort, Selection Sort and Insertion Sort

# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print("Bubble Sort - Pass", i + 1, ":", arr)

    return arr


# Selection Sort
def selection_sort(arr):
    arr = arr.copy()

    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Selection Sort - Step", i + 1, ":", arr)

    return arr


# Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print("Insertion Sort - Step", i, ":", arr)

    return arr


# Testing all three algorithms
sample_array = [5, 2, 8, 1, 9]

print("Original Array:", sample_array)

print("\n--- Bubble Sort ---")
bubble_result = bubble_sort(sample_array)
print("Final Bubble Sort:", bubble_result)

print("\n--- Selection Sort ---")
selection_result = selection_sort(sample_array)
print("Final Selection Sort:", selection_result)

print("\n--- Insertion Sort ---")
insertion_result = insertion_sort(sample_array)
print("Final Insertion Sort:", insertion_result)