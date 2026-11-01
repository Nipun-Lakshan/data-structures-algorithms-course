# Sorting Algorithm 04: Quick Sort
# ================================

# Part 01: Ascending Order
# ========================

# Define an Index For Step
i = 1

# Function to Perform Swapping
def quick_sort_ascending_swap(start_index, end_index, arr):
    if start_index != end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp

# Function to Perform Partition
def quick_sort_ascending_partition(arr, start_index, end_index):
    global i

    pivot_index = start_index
    pivot = arr[pivot_index]

    start_index = pivot_index + 1

    while start_index <= end_index:

        while start_index <= end_index and arr[start_index] <= pivot:
            start_index += 1

        while start_index <= end_index and arr[end_index] > pivot:
            end_index -= 1

        if start_index < end_index:
            quick_sort_ascending_swap(start_index, end_index, arr)

    quick_sort_ascending_swap(pivot_index, end_index, arr)
    print("Step", i, ":", arr)
    i += 1

    return end_index

# Function to Perform Quick Sort in Ascending Order
def quick_sort_ascending(arr, start_index, end_index):
    if start_index < end_index:
        partition_index = quick_sort_ascending_partition(arr, start_index, end_index)
        quick_sort_ascending(arr, start_index, (partition_index - 1))
        quick_sort_ascending(arr, (partition_index + 1), end_index)

# Part 02: Descending Order
# =========================

# Function to Perform Swapping
def quick_sort_descending_swap(start_index, end_index, arr):
    if start_index != end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp

# Function to Perform Partition
def quick_sort_descending_partition(arr, start_index, end_index):
    global i

    pivot_index = start_index
    pivot = arr[pivot_index]

    start_index = pivot_index + 1

    while start_index <= end_index:

        while start_index <= end_index and arr[start_index] >= pivot:
            start_index += 1

        while start_index <= end_index and arr[end_index] < pivot:
            end_index -= 1

        if start_index < end_index:
            quick_sort_descending_swap(start_index, end_index, arr)

    quick_sort_descending_swap(pivot_index, end_index, arr)
    print("Step", i, ":", arr)
    i += 1

    return end_index

# Function to Perform Quick Sort in Descending Order
def quick_sort_descending(arr, start_index, end_index):
    if start_index < end_index:
        partition_index = quick_sort_descending_partition(arr, start_index, end_index)
        quick_sort_descending(arr, start_index, (partition_index - 1))
        quick_sort_descending(arr, (partition_index + 1), end_index)

# Main Programme
if __name__ == '__main__':

    # Print the Main Header
    print("\n====================")
    print("Quick Sort Algorithm")
    print("====================\n")

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
    quick_sort_ascending(arr, 0, (len(arr) - 1))

    # Print the Sorted Array
    print()
    print("Sorted Array:", arr)

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

    # Define an Index for Steps
    i = 1

    # Call the Sorting Function
    quick_sort_descending(arr, 0, (len(arr) - 1))

    # Print the Sorted Array
    print()
    print("Sorted Array:", arr)