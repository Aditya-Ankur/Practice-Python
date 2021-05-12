import random

print("This is a dice simulator")
print("You and computer will roll a die \nThe entity whose number is greater wins")

probability_ofdie_comp = [1,2,3,4,5,6]
comp_points = 0
pl_points = 0
chances = 10
act_chance = 0
probability_ofdie_user = [1,2,3,4,5,6]

while act_chance < chances:
    
    user_input = input("\nType r to roll a die : ")
    if user_input == "r":
        comp_die = random.choice(probability_ofdie_comp)
        user_die = random.choice(probability_ofdie_user)
        
        # If computer wins

        if comp_die > user_die:
            print(f"\n{comp_die} vs {user_die}")
            print("You freaking nerd! You lost it")
            comp_points = comp_points + 1
            print(f"Computer's points = {comp_points} \nYour points = {pl_points}\n")
            act_chance = act_chance + 1
            continue
        
        # if user wins

        elif comp_die < user_die:
            print(f"\n{comp_die} vs {user_die}")
            print("You got it man! You won")
            pl_points = pl_points + 1
            print(f"Computer's points = {comp_points} \nYour points = {pl_points}\n")
            act_chance = act_chance + 1
            continue

        # if the match is tied

        else:
            print(f"\n{comp_die} vs {user_die}")
            print("Thats a freaking tie!")
            pl_points = pl_points + 1
            comp_points = comp_points + 1
            print(f"Computer's points = {comp_points} \nYour points = {pl_points}\n")
            act_chance = act_chance + 1
            continue
    else:
        print("Can't you see. Enter the freaking correct input!")
        continue

# After the game is over

print("Game Over")

if comp_points > pl_points:
    print("You are a freaking loser!")
    print(f"You lost it by {comp_points-pl_points} points")

elif comp_points < pl_points:
    print("My Algorithms were lineant thats why you won! Now get the hell out of here")
    print(f"You won it by {pl_points-comp_points} points")

else:
    print("You are such a freaking loser! You can't win it even the algorithms are lineant")
    print(f"Computer's points = {comp_points} \nYour points = {pl_points}")