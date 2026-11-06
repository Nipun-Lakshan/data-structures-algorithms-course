# Sorting Algorithm 06: Heap Sort
# ===============================

# Global Step Counter
step = 1

# Part 01: Ascending Order
# ========================

def heap_sort_swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heap_shift_down(arr, i, upper):
    while (True):

        left = (i * 2) + 1
        right = (i * 2) + 2

        if max(left, right) < upper:

            if arr[i] >= max(arr[left], arr[right]):
                break

            elif arr[left] > arr[right]:
                heap_sort_swap(arr, i, left)
                i = left

            else:
                heap_sort_swap(arr, i, right)
                i = right

        elif left < upper:

            if arr[left] > arr[i]:
                heap_sort_swap(arr, i, left)
                i = left

            else:
                break

        else:
            break


def heap_sort_ascending(arr):
    global step

    for j in range((len(arr) - 2) // 2, -1, -1):
        heap_shift_down(arr, j, len(arr))

    for end in range(len(arr) - 1, 0, -1):
        heap_sort_swap(arr, 0, end)
        heap_shift_down(arr, 0, end)
        print("Step", step, ":", arr)
        step += 1

# Part 02: Descending Order
# =========================

def heap_shift_down_descending(arr, i, upper):
    while (True):

        left = (i * 2) + 1
        right = (i * 2) + 2

        if max(left, right) < upper:

            if arr[i] <= min(arr[left], arr[right]):
                break

            elif arr[left] < arr[right]:
                heap_sort_swap(arr, i, left)
                i = left

            else:
                heap_sort_swap(arr, i, right)
                i = right

        elif left < upper:

            if arr[left] < arr[i]:
                heap_sort_swap(arr, i, left)
                i = left

            else:
                break

        else:
            break


def heap_sort_descending(arr):

    global step

    for j in range((len(arr) - 2) // 2, -1, -1):
        heap_shift_down_descending(arr, j, len(arr))

    for end in range(len(arr) - 1, 0, -1):
        heap_sort_swap(arr, 0, end)
        heap_shift_down_descending(arr, 0, end)
        print("Step", step, ":", arr)
        step += 1

# Main Programme
if __name__ == '__main__':

    # Print the Main Header
    print("\n===================")
    print("Heap Sort Algorithm")
    print("===================\n")

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
    heap_sort_ascending(arr)

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

    # Define Step Counter
    step = 1

    # Call the Sorting Function
    heap_sort_descending(arr)

    # Print the Sorted Array
    print()
    print("Sorted Array:", arr)