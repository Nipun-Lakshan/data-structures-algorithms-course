# Assignment 01: Question 07 - Find a Matching Value
# ==================================================

print("\n=====================")
print("Find a Matching Value")
print("=====================\n")

list_of_numbers = []
i = 0

try:
    N = int(input("Enter the size of the list (>0) : "))
    if N <= 0:
        print("Please enter a positive integer!")
    else:
        print("\n================================")
        print("Enter the Integers For the List")
        print("================================\n")
        while N > 0:
            try:
                i += 1
                N -= 1
                temp = int(input("Enter the " + str(i) + " Number of the list: "))
                if temp <= 0:
                    print("Please enter a positive integer!")
                    i -= 1
                    N += 1
                else:
                    list_of_numbers.append(temp)
            except ValueError:
                print("Wrong Number Format!")
                i -= 1
                N += 1
        print("\nList : " + str(list_of_numbers))
        print("\nList created successfully!\n")
        try:
            target = int(input("Enter the target number: "))
            if target <= 0:
                print("Please enter a positive integer!")
            else:
                boolean = True
                for i in range(0, len(list_of_numbers)):
                    if list_of_numbers[i] == target:
                        print("Match is Found! Index: " + str(i))
                        boolean = False
                        break
                if boolean == True:
                    print("Match is not Found!")
        except ValueError:
            print("Wrong Number Format!")
except ValueError:
    print("Wrong Number Format!")
finally:
    print("\nThank you for using this program!")