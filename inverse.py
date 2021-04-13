# This program enters a real number from the user and prints its additive inverse and multiplicative inverse
import sys
print("This program will find the additive or multiplicative inverse of the given number")

def add_inv():
    '''This function will calclate the fricking additive inverse of the user input'''

    user_no = float(input("Enter a real number : "))
    final_no = user_no * -1
    print(f"The additive inverse of {user_no} is {final_no}")
    recursion()

def multi_inv():
    '''This function will calculate the multiplicative inverse of the idiot's(I mean user) input'''

    user_no = float(input("Enter a real number : "))
    final_no = user_no ** -1
    print(f"The multiplicative inverse of {user_no} is {final_no}")
    recursion()    

def recursion():
    '''This will ask wheather the idiot wants to check again or not'''

    ask_q = input("Do you want to check another number? : ")
    if ask_q == "yes" or ask_q == "y" or ask_q == "yeah" or ask_q == "yooo":
        ques()
    elif ask_q == "no" or ask_q == "n" or ask_q == "nah":
        print("\nGet the hell out of here!")
        sys.exit()
    else:
        print("\nCan't you just see! Enter the freaking correct input\n")
        recursion()

def ques():
    '''This asks the idiot a choice to make between those two functions'''

    print("Press 1 on your goddamn!! keyboard for Additive inverse \nPress 2 on your goddamn!! keyboard for Multiplicative inverse")
    ask = int(input("Enter your fricking answer! : "))

    if ask == 1:
        add_inv()
    if ask == 2:
        multi_inv()
    else:
        print("Just enter the goddamn correct input you idiot!")
        ques()

ques()