import sys
print("This program will print all the factors of the chosen number by the user")


def get_factors():
    x = int(input("Enter the number : "))
    li = []
    for i in range(1, x + 1):
        if x % i == 0:
            li.append(i)
    print(li)
    recursion()

def recursion():
    print("\nWanna do that again?")
    print("Press 1 for Yes")
    print("Press 0 for No")
    ans = int(input("Enter your answer : "))

    if ans == 1:
        get_factors()
    elif ans == 0:
        print("Get the heck out of here!")
        sys.exit()
    else:
        print("Can't you enter a fricking valid answer!!")
        recursion()

get_factors()