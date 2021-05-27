# this program will check whether a given input is an Armstrong Number

def arms(num):
    li = [int(i) for i in str(num)]
    exp = len(li)
    arm = 0
    for index in range(exp):
        li[index] = li[index] ** exp
        arm = arm + li[index]
    return arm

def listArms():
    '''Returns a list of Armstrong numbers in a given range'''
    
    lst = []
    ll = int(input("Enter the lower limit of your search : "))
    ul = int(input("Enter its upper limit : "))
    li = [i for i in range(ll,ul+1)]

    for i in li:
        num = arms(i)
        if num == i:
            lst.append(num)
    print(lst)

print("Wanna check Armstrong Number or want a list of them in given range?")
print("Press 0 to check a number")
print("Press 1 to generate a list")
try:
    ans = int(input("Enter your answer : "))
    if ans == 0:
        n = int(input("Enter a number : "))
        if arms(n) == int(n):
            print(f"Yes, {n} is an Armstrong Number!!")
        else:
            print(f"{n} is not an Armstrong number.")
    elif ans == 1:
        listArms()
    else:
        print("Get lost you idiot!!")
except Exception:
    print("Get lost you idiot!!")