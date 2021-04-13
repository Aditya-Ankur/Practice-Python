print("This program will tell you if your entered number is a perfect square, cube or not")

li = list(range(0, 10000))

def ask():
    q = input("Wanna check again? : ")
    
    if q == "y" or q == "yes":
        expo()
    elif q == "n" or q == "no":
        print("Get lost!")
    else:
        print("Just give a fricking valid answer!\n")
        ask()
    
def expo():
    a = int(input("Enter the number : "))
    p = int(input("Enter the power you wanna check your number on : "))
    root = a **(1/p)
    
    if root in li:
        print(f"Yes, {a} is a perfect solution and the root is {root}")
        ask()
    else:
        print("No, its not a perfect solution")
        ask()

expo()


