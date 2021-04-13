print("This program will find the mean of the range of data given by the user")

li = []

x = int(input("Enter the starting value of the range : "))
y = int(input("Enter the ending value of the range : "))

for i in range(x, y + 1):
    li.append(i)
li.sort()
n = len(li)

mean = sum(li) / n
print(f"The data is : \n{li}")
print(f"\n\nThe mean is {mean}")

