# One of my favorite program till now. Took me so long to develop the logic and perform it
import os
import shutil

print("This program will print all the multiplication tables from 2 to 20 and will save them in a text file separately")

fname = input("Enter the name of the file you want to store tables in : ")

# From where the table will start
l = int(input("Enter the lower limit of your tables :"))  

# At where the table will end
u = int(input("Enter the upper limit of your tables : "))

os.mkdir(fname)    # it creates a directory in at the place where the program is saved

def table(n):
    '''This function writes the multiplication table into a '.txt' file and names it accordingly'''
    x = 1
    while x <= 10:
        f = open(f'table{n}.txt','a')
        f.write(f"{n} * {x} = {n*x}\n")
        x += 1
    f.close()

def files():
    '''This function creates multiplication table'''
    for i in range(l,u+1):
        table(i)

def move():
    '''This function moves all the files into a separate folder'''
    for i in range(l,u+1):
        source = f"table{i}.txt"
        shutil.move(source,fname)  # moves the created file into the designated folders


files()
move()





