print("This program will find the mean of the data given by the user")

li = []
n = int(input("Enter the number of terms you want to find the mean of : "))
for i in range(n):
    term = int(input("Enter the number : "))
    li.append(term)

mean = sum(li) / n
print(f"The mean of the following data \n{li} is {mean}")