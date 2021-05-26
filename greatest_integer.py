#this will return the greatest integer of some real number

greatestInt = lambda n : int(n // 1)

def recursion():
    try:
        num = float(input("Enter a number : "))
        print(f"Greatest Integer of {num} : {greatestInt(num)}")
    except Exception:
        print("You are a fricking fool, get lost")
        exit()
    try:
        ans = int(input("Wanna do that again?, if yes press 0 : "))
        if ans == 0:
            recursion()
    except ValueError:
        pass
recursion()