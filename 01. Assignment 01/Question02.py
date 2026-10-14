# Assignment 01: Question 02 - Calculate a Sum
# ============================================

print("\n===============")
print("Calculate a Sum")
print("===============\n")

total = 0

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        for i in range(1, N+1):
            total += i
        print("Sum of Numbers From 1 to", N, ":", total)
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")