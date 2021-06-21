# this program provides all the methods related to a student

import hashlib
import requirements as rq

class Student:
    def __init__(self):
        try:
            with open(f'Database/{nme}.txt') as f:
                content = f.readlines()

            print("You seem to be a member of the Library")    
            fetched = content[10]
            passlist = [i for i in fetched]
            passlist.remove('\n')
            truepass = "".join(passlist)

            password = input("Enter your password : ").encode('utf-8')
            password = bytes(password)

            res = hashlib.sha256(password)
            hashed = res.hexdigest()

            if str(hashed) == truepass:
                print("You are now logged in!\n")
            else:
                print("Invalid password")
                exit()
            
        except FileNotFoundError:
            ans = input("You are not a member of this library. Wanna sign up? if no press 'n' : ")
            if ans == 'n':
                exit()
            else:
                rq.signup(nme)
                
name = input("Enter your name : ")
nme = name
name = Student()