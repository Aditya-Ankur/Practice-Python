# this program has all the required functions for the main program

from books import fiction, nonfic, novels, selfhelp, beauty
import time
import datetime as dt
import hashlib
import os
import random

memberships = ['Broke', 'Rookie', 'Passionate', 'Pro', 'Elite']

def genCode():
    '''Generates a code for the log.txt'''

    choicesArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    codeArray = ['#']
    for i in range(0,8):
        codeArray.append(random.choice(choicesArray))
    logCode = ''.join(str(item) for item in codeArray)
    return logCode

def getbooks(ans):
    '''Prints all the books available'''

    if ans == 0:
        print(f"There are {len(beauty)} books available : \n")
        for index,content in enumerate(beauty):
            print(f"{index + 1} - {content}")
    
    elif ans == 1:
        print(f"There are {len(nonfic)} books available : \n")
        for index,content in enumerate(nonfic):
            print(f"{index + 1} - {content}")
    
    elif ans == 2:
        print(f"There are {len(novels)} books available : \n")
        for index,content in enumerate(novels):
            print(f"{index + 1} - {content}")
    
    elif ans == 3:
        print(f"There are {len(fiction)} books available : \n")
        for index,content in enumerate(fiction):
            print(f"{index + 1} - {content}")
    
    elif ans == 4:
        print(f"There are {len(selfhelp)} books available : \n")
        for index,content in enumerate(selfhelp):
            print(f"{index + 1} - {content}")
    else:
        print("Can't you enter a correct answer")
        exit()

def signup(nme):
    '''Signs a student up for the library'''
    
    print("Plans -\n\n")
    print("Broke(0) \n\t10$ a month \n\tRent Duration - 3 days \n\tMaximum - 2 books")
    print("Rookie(1) \n\t25$ a month \n\tRent Duration - 7 days \n\tMaximum - 5 books")
    print("Passionate(2) \n\t40$ a month \n\tRent Duration - 14 days \n\tMaximum - 10 books")
    print("Pro(3) \n\t70$ a month \n\tRent Duration - 30 days \n\tMaximum - 20 books")
    print("Elite(4) \n\t200$ a month \n\tRent Duration - 1 year \n\tMaximum - infinite")

    answer = int(input("Enter your choice, press 10 if you want to exit : "))
    if answer == 10:
        exit()
    else:
        email = input("Enter your email : ")
        
        password = input("Enter your new password : ").encode('utf-8')
        password = bytes(password)
        res = hashlib.sha256(password)
        hashed = res.hexdigest()

        contfirm = input("Press Enter to confirm the transaction : ")
        if contfirm == "":
            print("\nProcessing...\n")
            time.sleep(3)
            print("Transaction Successful.")
            print(f"You are now an {memberships[answer]} member of the Library")
    with open('signupToken.txt','w') as file:
        file.write(str(True))
    
    content = [
        'Email : \n',
        '',
        '\n\nSubscription Code : \n',
        '',
        '\n\nDate at which membership was purchased : \n',
        f'{dt.datetime.now()}\n',
        '\nEncrypted Password : \n',
        '',
        '\n\nBooks issued : \n',
        '']
    content[1] = email
    content[3] = str(answer)
    content[7] = str(hashed)
    content[9] = 'None'
    
    isfolder = False
    while isfolder == False:
        try:
            with open(f'Database/{nme}.txt','w') as f:
                f.writelines(content)
                isfolder = True
        except FileNotFoundError:
            os.mkdir('Database')
