# Assignment 01: Question 10 - Mixed Loop Analysis
# ================================================

print("\n===================")
print("Mixed Loop Analysis")
print("===================\n")

try:
    N = int(input("Enter a Number [N > 0] : "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer!")
    else:
        print("\n=========================")
        print("Print Numbers From 1 to N")
        print("=========================\n")
        for i in range(1, N+1):
            print(str(i) + ", ", end="")
        print("\b\b\n", end="")
        print("\n===========================")
        print("N x N Grid Coordinate Pairs")
        print("===========================\n")
        for i in range(1, N+1):
            for j in range(1, N+1):
                print("(" + str(i) + ", " + str(j) + ")" + ", ", end="")
            print("\b\b")
except ValueError:
    print("Wrong Format. Try again!")
finally:
    print("\nThank you for using this program!")
