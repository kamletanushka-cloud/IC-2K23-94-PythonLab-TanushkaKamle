# Section C - Program 4
# Iterative Binary Search


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Testing Binary Search

sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

# Value that exists
target1 = 23
result1 = binary_search(sorted_array, target1)

print("Array:", sorted_array)
print("Searching for:", target1)

if result1 != -1:
    print("23 found at index:", result1)
else:
    print("23 not found")


# Value that does not exist
target2 = 50
result2 = binary_search(sorted_array, target2)

print("\nSearching for:", target2)

if result2 != -1:
    print("50 found at index:", result2)
else:
    print("50 not found")