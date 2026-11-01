# Assignment 01: Question 04 - Find a Power of Two
# ================================================

print("\n===================")
print("Find a Power of Two")
print("===================\n")

value = 1
iterations = 0

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        while value <= N:
            value *= 2
            iterations += 1
        print("Numbers of iterations:", iterations)
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")