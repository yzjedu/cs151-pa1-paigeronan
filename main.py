# Programmer:Paige
# Course:CS*151
# Due Date:10/09/2024
# Assignment: pa01
# Problem Statement:
# Data In:
# Data Out:
# Credits:

print("You are about to go on an adventure in the woods!")

name = input("What is your name? ")
print("Hello", name, ", answer the questions to see what your adventure will be!")

direction = input("You start at a fork in the road, do you want to turn left or right?")
if direction == "left":
    print("After going to the left, you find a lake")
    swim_learn = input("Do you know how to swim?")
    swim_learn = swim_learn.lower()
    if swim_learn == "yes":
        print("Awsome!")
        age_swim = float(input("What age did you learn how to swim?"))
        swim = input("Do you want to swim in the lake?")
        if not swim == "yes":
            print("You dont swim in the lake.")
        else:
            print("You swim in the lake.")
    elif swim_learn == "no":
        print("You do not swim in the lake.")
elif direction == "right":
    print("After going right you are faced with 3 paths ahead.")
    pick_number = int(input("To determine which path you take, enter a number 1-10:"))
    if pick_number <= 3 and pick_number >= 1:
        print("You take the path to the left.")
        print("The left path takes you to two houses, one red and one blue")
        color = input("What color do you prefer, 'red' or 'blue'?")
        if color == "red":
            print("You go into the red house")
        elif color == "blue":
            print("You go into the blue house")
        else:
            print("That was not one of the options.")
    elif pick_number < 3 and pick_number <= 7:
        print("You take the middle path")
        print("You come across a pack of wolves and get scared. You run back to the start.")
    elif pick_number > 7 and pick_number <= 10:
        print("You take the path to the right and find an apple tree!")
        apple = input("What is your favorite apple?")
        print("You pick the", apple, "apple off the tree and eat it")
print("That is the end of your adventure.")
print("Thank you for playing my game!")
