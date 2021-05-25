'''For those who don't know what Hangman is,
Hangman is a game in which you have to guess a word.
The word is written in blank spaces.
You start by guessing a letter and the word chooser tells if your chosen letter is in the word or not.
If it is the 2nd person fills all the instances of that letter in the blank space.
You might have finite guesses and in this program you have finite number of guesses.
You win when you complete the word.

I have written it my myself, I didn't copied it xD!
Show some respect man!'''

#CODE
#As far as I can see,
#This code is not efficient but it just works and that's fine for me
#took so long to write and most of the time I was just removing the errors and thinking what to do to make it work

# importing list of words from 'words.py'
from words import words
import os
import random
import datetime as dt
import sys

name = input("Enter your name : ")

class Game:
    '''This class will provide logic to the game'''
    
    #this function will run even if it is not called
    def __init__(self):
        print("Welcome to the Hangman")
        print("Difficulty")
        print("0 - Peaceful")
        print("1 - Challenging")
        print("2 - Overwhelming")
        
        #global variable means they can be used outside the function
        global diff
        try:
            diff =  int(input("What difficulty you wanna play : "))
        except Exception:
            print("Enter a valid input you fool!")
            diff =  int(input("What difficulty you wanna play : "))
        finally:
            self.difficulty()
            print("The game begins now")
            print(f"The length of the word is {len(word)}\n")
            self.guess()

    def difficulty(self):
        '''It sets the difficulty according to the user's liking'''
        
        global word
        global guesses
        if diff == 0:
            guesses = 30
            #it will run until it finds a word less than equal to 5 characters
            while True:
                word = random.choice(words)
                if len(word) >= 5:
                    word = random.choice(words)
                else:
                    break
        
        elif diff == 1:
            guesses = 25
            #it will run until it finds a word less than 11 and more than 5 characters
            while True:
                word = random.choice(words)
                if len(word) >= 6 and len(word) <= 10:
                    break
                else:
                    word = random.choice(words)

        elif diff == 2:
            guesses = 21
            #it runs until it finds a word with more than 11 characters
            while True:
                word = random.choice(words)
                if len(word) < 11:
                    word = random.choice(words)
                else:
                    break
        else:
            print("Why the frick you didn't enter a valid input.")
            #exits the system right away terminating execution
            sys.exit()
    
    def print_word(self):
        '''Prints the current status of the word'''

        global dash
        try:
            with open('dash_num.txt') as f:
                    dash_num = f.read()
            with open('list.txt') as f:
                    global word_content
                    word_content = f.read()
                    list_word = [i for i in word_content]
            with open('dash.txt') as f:
                    global dash_content
                    dash_content = f.read()
                    dash = [i for i in dash_content]
        except Exception as error:
            dash_num = 0
        
        if dash_num == 0:
            dash = ["_" for i in word]
            list_word = [i for i in word]
        
        with open('list.txt','w') as f:
                    for i in list_word:
                            f.write(i)
        
        with open('dash_num.txt','w') as f:
            #for the 1st time dash_num will be 0
            #so it adds 1 to the int of dash_num and then typecast it into a str in order to write into a file
            #for 2nd time, 3rd time and so on
            #it will always execute the try code
            f.write(str(int(dash_num) + 1))
        
        #enumerate function runs two for loop one for the item in list_word and one for the index
        #index belongs to N and is in range of [0, infinity)
        #for this program index only goes upto the length of word randomly chosen
        for index,lt in enumerate(list_word):
            if lt == letter:
                    dash[index] = lt
        
        with open('dash.txt','w') as f:
            for i in dash:
                f.write(i)
        st = ""
        #some_string.join(some_list) makes a string and joins every element of the some_list with some_string
        print(st.join(dash))
    
    def winner(self):
        '''Declares the winner and prints some additional comments'''

        with open('list.txt') as f:
            lcontent = f.read()
        with open('dash.txt') as f:
            dcontent = f.read()
        
        # it checks both files and if they match, it clearly indicates that user has completed the game
        if lcontent == dcontent:
            if diff == 0 or diff == 1:
                print("A 12yo kid can even win on this easy difficulty LolXD!, HaHaHa!!")
                print(f"You had {actual_guess} guesses left.")
            else:
                print("Ohh Boi!!, you possess some sick vocabulary dude")
                print(f"You had {actual_guess} guesses left.")
        else:
            if diff == 0 or diff == 1:
                print("You are such a freaking loser. Can't even win on such easy difficulty. Don't ever come in my sight")
                print(f"That word is {word_content}")
            else:
                print("Wanna be the smart guy, HaHa!!. Go play on peaceful lol!")
                print(f"That word is {word_content}")

    def guess(self):
        '''Runs a loop of guesses input by the user until user wins or has no guesses left'''

        print(f"\nYou have {guesses} guesses")
        global actual_guess
        actual_guess = guesses
        global letter

        while actual_guess >= 1:
            try:
                with open('list.txt') as f:
                    li_content = f.read()
                with open('dash.txt') as f:
                    ds_content = f.read()
                #if the user is smart af, he/she might guess it correctly before guesses get over
                #so this is to prevent running of loop when user wins
                if ds_content == li_content:
                    break
            
            # for the first time, there will be no file hence, in order to not run into an error I have written and Exception
            except FileNotFoundError:
                pass
            
            letter = input("Enter your guess : ")
            #actual_guess decrements every time as the user guesses
            actual_guess = actual_guess - 1
            
            if letter in word:
                print(f"Oh Boi!, you guessed it right. You have {actual_guess} guesses left\n")
                self.print_word()
            elif letter is int or letter is float:
                print("Enter a fricking letter you fool not a number!")
            elif letter not in word and letter is str:
                print(f"You guessed it wrong. You have {actual_guess} guesses left\n") 
            else:
                print("Enter a valid input you fool")
                letter = input("Enter your guess : ")
        self.winner()

class Player:
    '''Handles player related functions like creating a log file for user's high scores'''

    def __init__(self):
        try:
            file = open('gamedata.txt')
            isFirstTime = False
            file.close()
        except FileNotFoundError:
            isFirstTime = True

        if isFirstTime == True:
            #in order for program to run, this is needed otherwise the indexing code will just throw an error
            #'index not in range'    
            with open('gamedata.txt','w') as f:
                f.write('\t\tHighscore at Peaceful\n\n')
                f.write('buffer data\n' * 3)
                f.write('0')
                
                f.write('\n\n\t\tHighscore at Challenging\n\n')
                f.write('buffer data\n' * 3)
                f.write('0')
                
                f.write('\n\n\t\tHighscore at Overwhelming\n\n')
                f.write('buffer data\n' * 3)
                f.write('0')        
        #runs self.funcname()
        #self here means Hangman
        self.high_score()
        self.gamedata()

    def gamedata(self):
        '''Saves the game data like the time at which highscore was made and the name of the player, etc in a separate text file'''

        if isHighscore == True:
            file = open('gamedata.txt')
            content = file.readlines()
            file.close()

            with open('gamedata.txt','w') as f:
                #changing the content of the file when highscore is created
                #for the first time buffer data is in the file and it is changed accordingly
                new_content = [i for i in content]
                if diff == 0:    
                    new_content[2] = f"Player's name : {name}\n"
                    new_content[3] = f"Time at highscore : {dt.datetime.now()}\n"
                    new_content[4] = "High Score :\n"
                    f.writelines(new_content)
                
                elif diff == 1:    
                    new_content[9] = f"Player's name : {name}\n"
                    new_content[10] = f"Time at highscore : {dt.datetime.now()}\n"
                    new_content[11] = "High Score :\n"
                    f.writelines(new_content)
                
                elif diff == 2:    
                    new_content[16] = f"Player's name : {name}\n"
                    new_content[17] = f"Time at highscore : {dt.datetime.now()}\n"
                    new_content[18] = "High Score :\n"
                    f.writelines(new_content)

    def high_score(self):
        '''Writes the highscore when created in a text file'''

        f = open('gamedata.txt')
        data_list = f.readlines()
        f.close()
        
        #backup list as write mode will just empty the file
        another_datalist = [i for i in data_list]
        global isHighscore
        
        #index of the highscore arbitrarily chosen by me for all the three difficulties
        if diff == 0:
            index = 5
        elif diff == 1:
            index = 12
        else:
            index = 19

        with open('gamedata.txt','w') as f:
            #overwrites the previous data at the index defined above
            if actual_guess > int(data_list[index]):
                data_list[index] = f"{actual_guess}\n"
                f.writelines(data_list)
                isHighscore = True
            else:
                f.writelines(another_datalist)
                isHighscore = False

#below statement has no real use in this program.
#I have just written it in order to do something fancy lol!!
if __name__ == "__main__":
    Hangman = Game()
    name = Player()

    # This is to delete the files that have been created during game
    def delete_files():
        os.remove('list.txt')
        os.remove('dash_num.txt')
        os.remove('dash.txt')
    delete_files()