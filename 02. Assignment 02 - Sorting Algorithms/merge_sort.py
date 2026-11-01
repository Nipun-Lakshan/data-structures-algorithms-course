# Sorting Algorithm 05: Merge Sort
# ================================

# Part 01: Ascending Order
# ========================

# Function to Merge Two Sorted Lists in Ascending Order
def merge_two_sorted_lists_ascending(left, right, arr):

    len_left = len(left)
    len_right = len(right)

    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

# Function to Perform Merge Sort in Ascending Order
def merge_sort_ascending(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort_ascending(left)
    merge_sort_ascending(right)

    merge_two_sorted_lists_ascending(left, right, arr)

    return arr

# Part 02: Descending Order
# =========================

# Function to Merge Two Sorted Lists in Descending Order
def merge_two_sorted_lists_descending(left, right, arr):

    len_left = len(left)
    len_right = len(right)

    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] >= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

# Function to Perform Merge Sort in Descending Order
def merge_sort_descending(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort_descending(left)
    merge_sort_descending(right)

    merge_two_sorted_lists_descending(left, right, arr)

    return arr

# Main Programme
if __name__ == '__main__':

    # Print the Main Header
    print("\n====================")
    print("Merge Sort Algorithm")
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

    # Call the Sorting Function
    merge_sort_ascending(arr)

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

    # Call the Sorting Function
    merge_sort_descending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", arr)