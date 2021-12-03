import random

# variables
miles_traveled = 0
hunger = 0
fatigue = 0
protectors_traveled = -20
bread_rations = 3
elven_village = 0
done = False


def print_instructions():
    print(' ')
    print("""Welcome to Forest.
You were exploring when you accident kicked a little mushroom house belonging to small fairy.
You stumble and try to apologize, but you have angered the nature spirits.
Now, you must make it out alive by navigating the woods.
Don't get captured by the woodland protectors!""")
    print(' ')


def main():
    print_instructions()


main()


while not done:
    protectors_behind = miles_traveled - protectors_traveled
    be_swift = random.randrange(7, 15)
    be_careful = random.randrange(1, 5)
    print("""
    A. Eat some elven bread.
    B. Move ahead carefully.
    C. Move ahead swiftly.
    D. Stop and rest for the night.
    E. Status check.
    Q. Quit.""")
    print(' ')
    user_input = input("What is your choice? ")
    print(' ')
    if user_input.upper() == "Q":
        print("Game over.")
        done = True


# status check
    elif user_input.upper() == "E":
        print("Miles traveled: ", miles_traveled)
        print("Elven bread rations left: ", bread_rations)
        print("You need", fatigue, "hours of sleep.")
        print("The woodland protectors are ", protectors_behind, "miles behind you.")
        print("Hunger:", hunger)

# stop and rest for the night
    elif user_input.upper() == "D":
        fatigue *= 0
        protectors_traveled += random.randrange(5, 7)
        print("You feel more energized and your fatigue is now", fatigue, ".")

# move ahead swiftly
    elif user_input.upper() == "C":
        print("You traveled", be_swift, "miles.")
        miles_traveled += be_swift
        hunger += 1
        fatigue += random.randrange(5, 8)
        protectors_traveled += random.randrange(5, 7)
        elven_village = random.randrange(1, 11)

# move ahead carefully
    elif user_input.upper() == "B":
        print("You traveled", be_careful, "miles.")
        miles_traveled += be_careful
        hunger += 1
        fatigue += 3
        protectors_traveled += random.randrange(5, 7)
        elven_village = random.randrange(1, 6)

# eat elven bread rations
    elif user_input.upper() == "A":
        if bread_rations == 0:
            print("You're out of bread rations, oh no!")
        else:
            bread_rations -= 1
            hunger *= 0
            print("You are no longer hungry.")
            print("You have", bread_rations, "rations of elven bread left.")

    else:
        print("Invalid input; Try again")

# not done check
    if elven_village == 4:
        fatigue *= 0
        hunger *= 0
        bread_rations = 3
        print("You found a friendly elven village. They have granted you a short stay.")
        print("Your rations have been restored, and you feel well-rested and full.")
    if protectors_behind <= 10:
        print("In the distance, you hear the woodland protectors thundering footsteps.")
    if miles_traveled >= 100 and not done:
        print("You have safely escaped the Forest!")
        done = True
    if protectors_traveled >= miles_traveled:
        print("The woodlands protectors have captured you and taken you to Mother Nature.")
        print("She is displeased. Good luck getting out of this one...")
        print("Game over.")
        done = True
    if hunger > 4 and hunger <= 6 and not done:
        print("Your stomach is grumbling, better eat something.")
    if hunger > 6:
        print("You starved.")
        print("Game over.")
    if fatigue > 10 and fatigue <= 15 and not done:
        print("Your feet begin to drag and you are getting very tired.")
        print("I would sleep soon.")
    if fatigue > 15:
        print("You fainted and can run no more.")
        print("Game over.")
        done = True
