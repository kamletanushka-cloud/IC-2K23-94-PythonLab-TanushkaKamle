# Section C - Program 3
# Radix Sort using LSD approach

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for number in arr:
        digit = (number // exp) % 10
        count[digit] += 1

    # Convert count into positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output


def radix_sort(arr):
    # Radix sort works with non-negative integers
    arr = arr.copy()

    if len(arr) == 0:
        return arr

    max_number = max(arr)
    exp = 1

    while max_number // exp > 0:
        arr = counting_sort(arr, exp)
        print("After sorting by digit place", exp, ":", arr)
        exp *= 10

    return arr


# Testing Radix Sort
sample_array = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original Array:", sample_array)

result = radix_sort(sample_array)

print("Final Sorted Array:", result)