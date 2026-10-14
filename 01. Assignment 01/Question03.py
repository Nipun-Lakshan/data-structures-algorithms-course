# Assignment 01: Question 03 - Count Even Numbers
# ===============================================

print("\n==================")
print("Count Even Numbers")
print("==================\n")

count = 0

try:
    N = int(input("Enter a positive integer (>0) : "))
    if N <= 0:
        print("Wrong Input! Enter a positive integer!")
    else:
        if N == 1:
            count = 1
            print("Count of Even Numbers from 2 including itself: 0")
        else:
            for i in range(1, N+1):
                if i % 2 == 0:
                    count += 1
            print("Count of Even Numbers from 2 including itself: " + str(count))
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")