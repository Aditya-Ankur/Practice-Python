# This program will provide train reservation and information class 
import random
import time
import string
import sys

class Railways:
    '''This will book a ticket, provide train and fare details for a train'''
    
    print("Welcome to Indian Railways")

    def search(train_number):
        '''This retreives and prints the information by the given train number'''

        li = ['Delhi','Mumbai','Bengaluru','Hyderabad','Lucknow','Jaipur','Jodhpur','Kota','Cochin','Guwahati','Darjeeling']

        src = random.choice(li)
        dst = random.choice(li)
        print(f"{dst} Express goes from {src} to {dst}")

    def fares(train_number):
        '''This will provide fare details of the given train'''

        li = [100,234,345,535,534,235,56,768,3457,345,56,3534,6432,453] #I just randomly slapped some keys for this

        tr_li = ['Delhi','Mumbai','Bengaluru','Hyderabad','Lucknow','Jaipur','Jodhpur','Kota','Cochin','Guwahati','Darjeeling']
        print(f"Fare of {random.choice(tr_li)} Express is {random.choice(li)}")

    def listTrains(source,destination):
        '''This will list all the trains that operate between the given source and destination'''

        trains = [12146, 17139, 15429, 13674, 15029, 12530, 14230, 17414, 17933, 19559] #here again
        ul = random.randint(0, 7)
        
        if ul == 0:
            print("No trains are available at this moment")
            sys.exit()
        else:
            for i in range(ul):
                print(f"{random.choice(trains)} is available from {source} to {destination}")

            ques = int(input("Wanna book seat, if yes press 1 and if no press 0: "))
            if ques == 1:
                train_number = int(input("Enter the train number in which you want to book a seat : "))
                Railways.book(train_number)
    
    def checkseat(train_number):
        '''This will provide seat details of the given train'''

        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 100)

        print(f"Number of lower birth seats available : {a}")
        print(f"Number of middle birth seats available : {b}")
        print(f"Number of upper birth seats available : {c}")
        print(f"Total seats available : {a+b+c}")
        
        ques = int(input("Wanna book seat, if yes press 1 and if no press 0: "))
        if ques == 1:
            Railways.book(train_number)

    def book(train_number):
        '''This function will book tickets of the specific given train'''

        li = []
        for i in string.ascii_uppercase:   #This makes a list of all the uppercase alphabets
            li.append(i)
        
        print("Which birth do you prefer")
        print("0 - lower birth")
        print("1 - middle birth")
        print("2 - upper birth")
        ans = int(input("Enter your answer : "))
        num = int(input("Enter the number of seat(s) you wanna book : "))

        #This is pile of repeated code with slight changes in them
        if ans == 0:
            price = random.randint(5000,10000)
            
            print(f"Lower birth seat costs {price}")
            print(f"Total price : {price*num}")
            paycon = int(input("Press 1 to confirm payment : "))
            if paycon == 1:
                print("Processing...")
                time.sleep(3)
                print("Payment made successfully")
                seat = ""
                
                for i in range(1,num+1):
                    seat = seat + str(i) + " - " + str(random.choice(li)) + str(random.randint(0, 100)) + "\n"
                if num == 1:
                    print(f"Your seat number is {random.choice(li)}{random.randint(0, 100)}")
                else:
                    print(f"Your seat numbers are as follows : \n{seat}")

        elif ans == 1:
            price = random.randint(1000,5000)
            
            print(f"Middle birth seat costs {price}")
            print(f"Total price : {price*num}")
            paycon = int(input("Press 1 to confirm payment : "))
            if paycon == 1:
                print("Processing...")
                time.sleep(3)
                print("Payment made successfully")
                seat = ""
                
                for i in range(1,num+1):
                    seat = seat + str(i) + " - " + str(random.choice(li)) + str(random.randint(0, 100)) + "\n"
                if num == 1:
                    print(f"Your seat number is {random.choice(li)}{random.randint(0, 100)}")
                else:
                    print(f"Your seat numbers are as follows : \n{seat}")

        elif ans == 2:
            price = random.randint(500,3000)
            print(f"Upper birth seat costs {price}")
            print(f"Total price : {price*num}")
            paycon = int(input("Press 1 to confirm payment : "))
            if paycon == 1:
                print("\nProcessing...\n")
                time.sleep(3)
                print("Payment made successfully")
                seat = ""
                
                for i in range(1,num+1):
                    seat = seat + str(i) + " - " + str(random.choice(li)) + str(random.randint(0, 100)) + "\n"
                if num == 1:
                    print(f"Your seat number is {random.choice(li)}{random.randint(0, 100)}")
                else:
                    print(f"Your seat numbers are as follows : \n{seat}")

#Here you can give actual instructions
#for example

# Railways.search(11010)
# Railways.fares(11010)
# Railways.listTrains('Delhi','Guwahati')
# Railways.checkseat(11010)
# Railways.book(11010)
