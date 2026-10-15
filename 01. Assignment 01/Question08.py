# Assignment 01: Question 08 - Compare Two Lists
# ==============================================

def compare(list_1, list_2):
    print("List 01: " + str(list_1))
    print("List 02: " + str(list_2))
    if len(list_1) != len(list_2):
        print("\nLists are not equal!")
        print("\nThank you for using this program!")
    else:
        for i in range(0, len(list_1)):
            for j in range(0, len(list_2)):
                if list_1[i] == list_2[j]:
                    print("\nMatch is Found! Index of List 1: " + str(i) + " & " + "Index of List 2: " + str(j))
                    print("Value: " + str(list_1[i]))
                    return
        else:
            print("\nMatch is not Found!")

if __name__ == "__main__":

    print("\n=================")
    print("Compare Two Lists")
    print("=================\n")

    list_1 = [12, 99, 97, 852, 63, 98, 78]
    list_2 = [15, 18, 93, 789, 46, 89, 78]

    compare(list_1, list_2)