# Sorting Algorithm 03: Selection Sort
# ====================================

# Part 01: Ascending Order
# ========================

# Function to Perform Selection Sort in Ascending Order
def selection_sort_ascending(arr):
    n = len(arr)

    for i in range(0, n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        print("Step", (i+1), ":", arr)

    return arr

# Part 02: Descending Order
# =========================

# Function to Perform Selection Sort in Descending Order
def selection_sort_descending(arr):
    n = len(arr)

    for i in range(0, n-1):
        max_index = i

        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

        print("Step", (i+1), ":", arr)

    return arr

# Main Programme
if __name__ == '__main__':

    # Print the Main Header
    print("\n========================")
    print("Selection Sort Algorithm")
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
    sorted_array_ascending = selection_sort_ascending(arr)

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
    sorted_array_descending = selection_sort_descending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", sorted_array_descending)