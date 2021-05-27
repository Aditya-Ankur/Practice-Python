# this will calculate the fractional part of a given input

fractPart = lambda n : n - (n // 1)

def recursion():
    try:
        num = float(input("Enter a number : "))
        fpart = round(fractPart(num),1)
        print(f"Fractional part of {num} : {fpart}")
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
