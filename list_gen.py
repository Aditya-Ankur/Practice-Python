# This program will generate and print numbers according to user's choice
import random

print("\nWrite the starting and ending number in the list and you will get the list printed according to your liking")

a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))

print("\n\nWhat do you want to do with this list?")
print("\nPress 1 to print all items in the list")
print("\nPress 2 to print even items in the list")
print("\nPress 3 to print odd items in the list")
print("\nPress 4 to print the list in descending order")
print(f"\nPress 5 to print all the numbers in between the range of {a} and {b} : ")
print(f"\nPress 6 to print your lucky number from the given list")
print(f"\nPress 7 to print your 3 luckiest numbers from the given list")

print(f"\nPress 8 to print all the numbers in the range of {a} and {b} divisible by your chosen number\n\n") 
ans = int(input("Enter your answer : "))

def list_all():
    x = list(range(a, b+1))  
    x.sort()
    print(x, end = " ")
    
def list_even():
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end = " ")

def list_odd():
    for i in range(a, b+1):
            if i % 2 != 0:
                print(i, end = " ")

def list_descending():
    x = list(range(a, b+1))  
    x.sort(reverse=True)
    print(x, end = " ")

def list_inbetween():
    x = list(range(a+1, b))
    x.sort()
    print(x, end = " ")

def list_divisible():
    x = int(input("Enter your chosen number : "))
    for i in range(a, b+1):
        if i > 1:
            if i % x == 0:
                print(i, end = " ")

def list_lucky():
    x = list(range(a, b+1))
    x.sort()
    l = random.choice(x)
    print(f"Your lucky number is {l}")

def list_mlucky():
    x = list(range(a, b+1))
    x.sort()
    l1 = random.choice(x)
    l2 = random.choice(x)
    l3 = random.choice(x)
    print(f"Your 3 luckiest number are : {l1}, {l2} and {l3}")

if ans == 1:
    list_all()

elif ans == 2:
    list_even() 

elif ans == 3:
    list_odd()

elif ans == 4:
    list_descending()

elif ans == 5:
    list_inbetween()

elif ans == 6:
    list_lucky()

elif ans == 7:
    list_mlucky()

elif ans == 8:
    list_divisible()
    
else:
    print("Can't you answer a freaking question in a valid way. Get Lost! you idiot.")
        