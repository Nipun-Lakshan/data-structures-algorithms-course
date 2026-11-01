# Sorting Algorithm 01: Bubble Sort
# =================================

# Part 01: Ascending Order
# ========================

# Function to Perform Bubble Sort in Ascending Order
def bubble_sort_ascending(arr):
    n = len(arr)

    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True

        if swapped == False:
            break
        print("Step", (i + 1), ": ", arr)

    return arr

# Part 02: Descending Order
# =========================

# Function to Perform Bubble Sort in Descending Order
def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True

        if swapped == False:
            break
        print("Step", (i+1), ": ", arr)

    return arr

# Main Function
if __name__ == '__main__':

    # Print the Main Header
    print("\n=====================")
    print("Bubble Sort Algorithm")
    print("=====================\n")

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
    sorted_array_ascending = bubble_sort_ascending(arr)

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
    sorted_array_descending = bubble_sort_descending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", sorted_array_descending)