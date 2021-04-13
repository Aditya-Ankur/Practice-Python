print("This is the program that reverses a string or a number entered by the user")
print("What is your input format")
print("Type str for string \nType int for integer")

user_input = input("Enter your answer : ")

def reverse_string():
    
    '''This will reverse the string input by the user'''

    act_str = input("Enter the string : ")
    split_text = act_str.split()
    li = []
    li.append(split_text)
    print(split_text)

reverse_string()

# if user_input == "str":


