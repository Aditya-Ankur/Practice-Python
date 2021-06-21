# the main program
# Library Management System - it provides all the methods to manage a library

from books import fiction, nonfic, novels, selfhelp, beauty
import requirements as rq
from student import Student, nme
import datetime
import os

class Library:
    def __init__(self):
        print("Welcome to the Library!!\n")
        print("What you wanna do?")
        print("\n0 to list books available")
        print("1 to search for a book")
        print("2 to rent a book")
        print("3 to return a book")
        print("4 to view profile")
        print("Enter to exit.")

        activity = '#login'
        self.log(activity)

        try:
            ans = int(input("Enter your answer : "))
            if ans == 0:
                self.listbooks()
            elif ans == 1:
                bookname = input("Enter the book name : ")
                self.search(bookname)
            elif ans == 2:
                self.rentbook()
            elif ans == 3:
                self.returnbook()
            elif ans == 4:
                self.profile()
        except Exception:
            exit()

    def listbooks(self):
        '''List all the books available'''    

        print("\nBook Genres : ")
        print("0 - Mathematics and Science")
        print("1 - Non-Fiction \n2 - Novels")
        print("3 - Fiction \n4 - Self-Help")

        ans = int(input("Enter your answer : "))
        rq.getbooks(ans)
        
        print("Wanna rent a book in here?")
        book = input("If yes enter the book name else Press Enter : ")
        if book == '':
            exit()
        else:
            self.rentbook(bookname = book)
    
    def search(self,book):
        '''Searches the library for the required book'''

        book = str(book).title()
        global isbook
        isbook = False

        for i in beauty:
            if book in i:
                print(f"{i} is available.")
                isbook = True
        for i in selfhelp:
            if book in i:
                print(f"{i} is available.")
                isbook = True
        for i in novels:
            if book in i:
                print(f"{i} is available.")
                isbook = True
        for i in fiction:
            if book in i:
                print(f"{i} is available.")
                isbook = True
        for i in nonfic:
            if book in i:
                print(f"{i} is available.")
                isbook = True
        if isbook == False:
            print(f"{book} is not available at the moment.")

    def profile(self):
        '''Prints the profile of the user'''

        with open(f'Database/{nme}.txt') as f:
                content = f.readlines()
        
        global days
        days = content[4]
        plan = rq.memberships[int(days)]

        booklist = []
        for i in range(13,len(content)):
            booklist.append(str(content[i]))
               
        print(f"\n\tName : {nme.title()}")
        print(f"\tEmail : {content[1]}\tSubscription Plan : {plan}")
        print(f"\tBooks issued : ")

        for j in booklist:
            j = str(j)         
            if j == 'None':
                print(f'\t{j}')
            elif '\n' in j:
                j.replace('\n','')
                print(f'\t{j}')
            else:
                print(f'\t{j}')


    def rentbook(self, bookname = None):
        '''This function will rent a book for the user'''
        
        if bookname == None:
            bookname = input("Enter the name of the book you wanna rent : ").title()
        else:
            bookname = str(bookname).title()
        
        with open(f'Database/{nme}.txt') as f:
            content = f.readlines()
            days = int(content[4])

        rentdays = ['3 days', '7 days', '14 days', '30 days', '1 year']
        duration = rentdays[days]
        isbook = False
        
        for i in nonfic:
            if bookname in i.title():
                print(f"{i} is now rented for you. Thanks!")
                print(f"You have {duration} left.")
                isbook = True
                bname = i
                activity = "#rentbook"
                book = bname
                self.log(activity, bookname=book)
                break
        for i in selfhelp:
            if bookname in i.title():
                print(f"{i} is now rented for you. Thanks!")
                print(f"You have {duration} left.")
                isbook = True
                bname = i
                activity = "#rentbook"
                book = bname
                self.log(activity, bookname=book)
                break
        for i in novels:
            if bookname in i.title():
                print(f"{i} is now rented for you. Thanks!")
                print(f"You have {duration} left.")
                isbook = True
                bname = i
                activity = "#rentbook"
                book = bname
                self.log(activity, bookname=book)
                break
        for i in fiction:
            if bookname in i.title():
                print(f"{i} is now rented for you. Thanks!")
                print(f"You have {duration} left.")
                isbook = True
                bname = i
                activity = "#rentbook"
                book = bname
                self.log(activity, bookname=book)
                break
        for i in beauty:
            if bookname in i.title():
                print(f"{i} is now rented for you. Thanks!")
                print(f"You have {duration} left.")
                isbook = True
                bname = i
                activity = "#rentbook"
                book = bname
                self.log(activity, bookname=book)
                break
        if isbook == False:
            print(f"{bookname} is not available at the moment.")
            exit()
        
        with open(f'Database/{nme}.txt') as f:
            cnt = f.readlines()
        
        if cnt[13] == 'None':
            cnt[13] = bname
        else:
            cnt.append(f'\n{bname}')
        
        with open(f'Database/{nme}.txt','w') as file:
            file.writelines(cnt)

    def returnbook(self):
        '''Returns rented books'''

        file = open(f'Database/{nme}.txt')
        content =  file.readlines()
        file.close()

        global rentedbooks
        rentedbooks = []
        for i in range(13, len(content)):
            if "\n" in content[i]:
                nthbook = content[i].replace("\n","")
            else:
                nthbook = content[i]
            rentedbooks.append(nthbook)
        print("\nYour rented books are : ")
        for index,item in enumerate(rentedbooks):
            print(f"{index} - {item}")

        print("Which book you wanna return?")
        question = int(input(("Enter 69 to return all books else enter book code : ")))
        if question == 69:
            newcontent = []
            for i in range(0,len(content)):
                if i == 13:
                    break
                else:
                    newcontent.append(content[i])
            print("Books returned.")
            newcontent.append(str(None))
            with open(f'Database/{nme}.txt','w') as f:
                f.writelines(newcontent)
            activity = '#returnbook'
            book = str(rentedbooks)
            self.log(activity, bookname=book)
        else:
            removedBookContent = []
            try:
                returnedBook = rentedbooks[question]
            except Exception:
                print("Enter a valid input you idiot.")
            else:
                for item in content:
                    if item == returnedBook or item == f"{returnedBook}\n":
                        pass
                    else:
                        removedBookContent.append(item)
                print(f"{returnedBook} returned.")
                with open(f'Database/{nme}.txt','w') as f:
                    f.writelines(removedBookContent)
            activity = '#returnbook'
            book = returnedBook
            self.log(activity, bookname=book)
            
    def log(self, activity, bookname = None):
        '''Logs the activity of the users'''
        
        username = nme.title()
        logCode = rq.genCode()
        time = datetime.datetime.now()
        try:
            with open('signupToken.txt') as file:
                token = file.read()  
            if token == str(True):
                with open('logfile.txt','a') as f:
                    f.write("Activity : #signup")
                    f.write(f"\nContent : '{username}' signed up for the library")
                    f.write(f"\nTime : {time}")
                    f.write(f"\nId : {rq.genCode()}\n\n")
            os.remove('signupToken.txt')
        except Exception:
            pass
        
        if activity == "#login":
            with open('logfile.txt','a') as f:
                f.write("Activity : #login")
                f.write(f"\nContent : '{username}' logged in to library")
                f.write(f"\nTime : {time}")
                f.write(f"\nId : {logCode}\n\n")
        
        elif activity == "#rentbook":
            with open('logfile.txt','a') as f:
                f.write("Activity : #rentbook")
                f.write(f"\nContent : '{username}' rented '{bookname}'")
                f.write(f"\nTime : {time}")
                f.write(f"\nId : {logCode}\n\n")
        
        elif activity == "#returnbook":
            with open('logfile.txt','a') as f:
                f.write("Activity : #returnbook")
                f.write(f"\nContent : '{username}' returned '{bookname}'")
                f.write(f"\nTime : {time}")
                f.write(f"\nId : {logCode}\n\n")
        
lib = Library()
