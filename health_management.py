# it uses datetime to track file changes
def getdate():
    import datetime
    return datetime.datetime.now()

# creating a function named log
def log(k):

    '''This function is used to log all the activities of the user to a respective file'''
   
    if k == 1:
        c = int(input("Enter 1 for diet and 2 for exercise : "))
        if c == 1:
            file_val = input("Enter your activity : ")
            with open("aditya_diet.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Succesfully")

        elif c == 2:
            file_val = input("Enter your activity : ")
            with open("aditya_ex.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Successfully")
    elif k == 2:
        c = int(input("Enter 1 for diet and 2 for exercise : "))
        if c == 1:
            file_val = input("Enter your activity : ")
            with open("ankur_diet.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Succesfully")
        elif c == 2:
            file_val = input("Enter your activity : ")
            with open("ankur_ex.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Successfully")
    elif k == 3:
        c = int(input("Enter 1 for diet and 2 for exercise : "))
        if c == 1:
            file_val = input("Enter your activity : ")
            with open("artemis_diet.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Succesfully")
        elif c == 2:
            file_val = input("Enter your activity : ")
            with open("artemis_ex.txt", "a") as fl:
                fl.write(str([str(getdate())]) + " : " + file_val + "\n")
                print("Written Successfully")
    else:
        print("You have passed an invalid argument. Get lost!")

def retrieve(k):

    '''This function is used to retrieve all the activities entered by the user on the specific datetime'''

    if k == 1:
        c = int(input("Type 1 for diet and 2 for exercise : "))
        if c == 1:
            with open("aditya_diet.txt") as fl:
                for i in fl:
                    print(i)                
        elif c == 2:
            with open("aditya_ex.txt") as fl:
                for i in fl:
                    print(i) 
        else:
            print("Enter a freaking valid input, You Idiot!!")
    elif k == 2:
        c = int(input("Type 1 for diet and 2 for exercise : "))                      
        if c == 1:
            with open("ankur_diet.txt") as fl:
                for i in fl:
                    print(i)
        elif c == 2:
            with open("ankur_ex.txt") as fl:
                for i in fl:
                    print(i)
        else:
            print("Enter a freaking valid input, You Idiot!!")
    elif k == 3:
        c = int(input("Type 1 for diet and 2 for exercise : "))
        if c == 1:
            with open("artemis_diet.txt") as fl:
                for i in fl:
                    print(i)
        elif c == 2:
             with open("artemis_ex.txt") as fl:
                for i in fl:
                    print(i)
        else:
            print("Enter a freaking valid input, You Idiot!!")

# Health Management System
print("Diet and Exercise Tracker")
print("1 for Aditya")
print("2 for Ankur")
print("3 for Artemis")
k = int(input("Enter your answer : "))

print("What do you want")
print("1 for log the data")
print("2 for retrieve the data")

def answer_x():
    x = int(input("Enter your answer : "))
    if x == 1:
        log(k)
    elif x == 2:
        retrieve(k)
    else:
        print("Can't you just give a freaking valid answer")
        answer_x()

answer_x()
