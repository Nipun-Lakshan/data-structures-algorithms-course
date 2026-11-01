# Assignment 01: Question 05 - Nested Loop: Pairs
# ===============================================

print("\n==================")
print("Nested Loop: Pairs")
print("==================\n")

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        print()
        for i in range(1, N+1):
            for j in range(1, N+1):
                print("(" + str(i) + "," + str(j) + ")")
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")