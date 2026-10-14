# Assignment 01: Question 01 - Display the Numbers
# ================================================

print("\n=============================")
print("Display All Numbers Programme")
print("=============================\n")

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        print("")
        for i in range(1, N+1):
            print(i)
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")