print("This program will reverse the given number or word")
print("Press 0 to reverse a number")
print("Press 1 to reverse a word")
ans = int(input("Enter your answer : "))



def reverse_num(x):
    li = []
    for i in x:
        li.append(int(i))
    
    li.reverse()
    print("Reversed Number : ")
    for j in li:
        print(j,end="")
    
# reverse_num(num)

def reverse_str(x):
    li = []
    for i in x:
        li.append(i)
    
    li.reverse()
    print("Reversed String : ")
    for j in li:
        print(j,end="")

if ans == 0:
    num = input("Enter the number : ")
    reverse_num(num)
elif ans == 1:
    string = input("Enter the string : ")
    reverse_str(string)
else:
    print("Can't you enter a fricking valid answer. Get lost!")