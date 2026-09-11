# Section E - Program 8
# Search Engine Simulator

# A dictionary of 30+ words with mock document IDs
words = {
    "algorithm": 101,
    "array": 102,
    "binary": 103,
    "computer": 104,
    "database": 105,
    "data": 106,
    "developer": 107,
    "function": 108,
    "graph": 109,
    "hashing": 110,
    "heap": 111,
    "index": 112,
    "java": 113,
    "keyword": 114,
    "machine": 115,
    "matrix": 116,
    "network": 117,
    "python": 118,
    "queue": 119,
    "recursion": 120,
    "search": 121,
    "software": 122,
    "sorting": 123,
    "stack": 124,
    "string": 125,
    "tree": 126,
    "variable": 127,
    "web": 128,
    "website": 129,
    "program": 130,
    "student": 131,
    "database": 132
}


# --------------------------------------------------
# Binary Search
# --------------------------------------------------

def binary_search(words_list, target):

    low = 0
    high = len(words_list) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2
        comparisons += 1

        if words_list[mid][0] == target:
            return words_list[mid][1], comparisons

        elif words_list[mid][0] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None, comparisons


# --------------------------------------------------
# Hash Function
# --------------------------------------------------

def hash_function(word, table_size):

    total = 0

    for character in word:
        total += ord(character)

    return total % table_size


# --------------------------------------------------
# Separate Chaining
# --------------------------------------------------

def create_chaining_table(words_list, table_size):

    table = [[] for _ in range(table_size)]

    for word, value in words_list:

        index = hash_function(word, table_size)

        table[index].append((word, value))

    return table


def chaining_search(table, target):

    index = hash_function(target, len(table))

    comparisons = 0

    for word, value in table[index]:

        comparisons += 1

        if word == target:
            return value, comparisons

    return None, comparisons


# --------------------------------------------------
# Linear Probing
# --------------------------------------------------

def create_probing_table(words_list, table_size):

    table = [None] * table_size

    for word, value in words_list:

        index = hash_function(word, table_size)

        while table[index] is not None:
            index = (index + 1) % table_size

        table[index] = (word, value)

    return table


def probing_search(table, target):

    index = hash_function(target, len(table))

    probes = 0
    start_index = index

    while table[index] is not None:

        probes += 1

        if table[index][0] == target:
            return table[index][1], probes

        index = (index + 1) % len(table)

        # Stop if we have checked the whole table
        if index == start_index:
            break

    return None, probes


# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main():

    words_list = sorted(words.items())

    table_size = 37

    chaining_table = create_chaining_table(
        words_list,
        table_size
    )

    probing_table = create_probing_table(
        words_list,
        table_size
    )

    print("===== Search Engine Simulator =====")

    print("\nAvailable words:")
    print(", ".join(words.keys()))

    target = input("\nEnter a word to search: ").lower()

    # Binary Search
    binary_result, binary_steps = binary_search(
        words_list,
        target
    )

    # Separate Chaining
    chaining_result, chaining_steps = chaining_search(
        chaining_table,
        target
    )

    # Linear Probing
    probing_result, probing_steps = probing_search(
        probing_table,
        target
    )

    print("\n===== Search Results =====")

    print("\n1. Binary Search")

    if binary_result is not None:
        print("Found!")
        print("Document ID:", binary_result)
    else:
        print("Word not found.")

    print("Comparisons:", binary_steps)

    print("\n2. Hash Table - Separate Chaining")

    if chaining_result is not None:
        print("Found!")
        print("Document ID:", chaining_result)
    else:
        print("Word not found.")

    print("Comparisons:", chaining_steps)

    print("\n3. Hash Table - Linear Probing")

    if probing_result is not None:
        print("Found!")
        print("Document ID:", probing_result)
    else:
        print("Word not found.")

    print("Probes:", probing_steps)


if __name__ == "__main__":
    main()