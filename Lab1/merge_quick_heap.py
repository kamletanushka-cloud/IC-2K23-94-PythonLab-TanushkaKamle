# Section C - Program 2
# Merge Sort, Quick Sort and Heap Sort


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
# Pivot strategy used: Last element
def quick_sort(arr):
    arr = arr.copy()

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)

            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr


# Heap Sort
def heap_sort(arr):
    arr = arr.copy()

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# Testing all three algorithms
sample_array = [8, 3, 5, 4, 7, 6, 1, 2]

print("Original Array:", sample_array)

print("\n--- Merge Sort ---")
merge_result = merge_sort(sample_array)
print("Sorted Array:", merge_result)

print("\n--- Quick Sort ---")
quick_result = quick_sort(sample_array)
print("Sorted Array:", quick_result)

print("\n--- Heap Sort ---")
heap_result = heap_sort(sample_array)
print("Sorted Array:", heap_result)