# Assignment 01: Question 06 - Nested Loop: Triangular Pattern
# ============================================================

print("\n===============================")
print("Nested Loop: Triangular Pattern")
print("===============================\n")

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        item = input("Enter a Symbol, Letter or Digit: ")
        if len(item) == 0:
            print("Wrong Input! The item cannot be empty string!.")
        elif len(item) > 1:
            print("Wrong Input! The length of the string should be one.")
        else:
            index = (int((N + (N-1))/2 + 0.5) - 1)
            print()
            for i in range(1, N+1):
                temp = (" " * index)
                print(temp, end="")
                for j in range(1, i+1):
                    print(item + " ", end="")
                index -= 1
                print()
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")