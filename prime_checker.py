print("This program is used to check wheather the number is prime or not")

def recursion():
    '''This will ask wheather the user wants to check again or not'''

    ask_q = input("Do you want to check another number? : ")
    if ask_q == "yes" or ask_q == "y":
        check_prime()
    elif ask_q == "no" or ask_q == "n":
        print("Get the hell out of here!")
    else:
        print("Can't you just see! Enter the freaking correct input")
        recursion()

def check_prime():
    '''This will check wheather the number input by the user is a prime number or not'''
    
    user_no = int(input("Enter the number : "))
    for number in range(2,user_no):
        if user_no % number == 0:
            print("Its not a prime number")
            break
        else:
            print("Its a prime number")
            break
    recursion()
check_prime()






        