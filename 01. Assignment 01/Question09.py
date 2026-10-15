# Assignment 01: Question 09 - Count the Number of Digits
# =======================================================

print("\n==========================")
print("Count the Number of Digits")
print("==========================\n")

count = 0

try:
    N = int(input("Enter a Number (>0): "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer!")
    else:
        if len(str(N)) == 1:
            print("\nNumber of Digits     : 1")
            print("Number of Iterations : 1")
        else:
            while len(str(N)) > 1:
                N = int(N/10)
                count += 1
            print("\nNumber of Digits     : " + str(count + 1))
            print("Number of Iterations : " + str(count + 1))
except ValueError:
    print("Wrong Format. Try again!")
finally:
    print("\nThank you for using this program!")
