# Sorting Algorithm 02: Insertion Sort
# ====================================

# Part 01: Ascending Order
# ========================

# Function to Perform Insertion Sort in Ascending Order
def insertion_sort_ascending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

        print("Step", i, ": ", arr)

    return arr

# Part 02: Descending Order
# =========================

# Function to Perform Insertion Sort in Descending Order
def insertion_sort_descending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print("Step", i, ": ", arr)

    return arr


# Main Programme
if __name__ == '__main__':

    # Print the Main Header
    print("\n========================")
    print("Insertion Sort Algorithm")
    print("========================\n")

    # Define the Input Array
    arr = [12, 8, 9, 3, 11, 5, 4]

    # Part 01: Ascending Order
    # ========================

    # Print the Subheading
    print("========================")
    print("Part 01: Ascending Order")
    print("========================\n")

    # Print the Original Array
    print("Original Array:", arr)
    print()

    # Call the Sorting Function
    sorted_array_ascending = insertion_sort_ascending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", sorted_array_ascending)

    # Define the Input Array
    arr = [12, 8, 9, 3, 11, 5, 4]

    # Part 02: Descending Order
    # =========================

    # Print the Subheading
    print("\n=========================")
    print("Part 02: Descending Order")
    print("=========================\n")

    # Print the Original Array
    print("Original Array:", arr)
    print()

    # Call the Sorting Function
    sorted_array_descending = insertion_sort_descending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", sorted_array_descending)