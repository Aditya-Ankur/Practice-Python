import random
print("This programs returns the total outcomes for the event given by the user")

print("Press 1 for Coin event")
print("Press 2 for Die event")
print("Press 3 for Card event")

ev_name = int(input("Enter your answer : "))

n = int(input("Enter the number of simultanious events happened : "))

def duplicate(x):
    return list(dict.fromkeys(x))

def coin():
    toss = []
    tt = 2 ** n     #Total outcomes
    
    if n == 1:
        for i in range(tt):
            n_coins = random.randint(0,1)
            toss.append(n_coins)
            duplicate(n_coins)
            print(toss, end=" ")
    elif n == 2:
        for i in range(tt):
            n_coins = random.randint(0,1), random.randint(0,1)
            toss.append(n_coins)
            duplicate(n_coins)
            print(toss, end=" ")
    elif n == 3:
        for i in range(tt):
            n_coins = random.randint(0,1), random.randint(0,1), random.randint(0,1)
            toss.append(n_coins)
            duplicate(n_coins)
            print(toss, end=" ")
    else:
        print("nothing")

coin()