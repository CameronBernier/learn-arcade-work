print("Welcome to the Quiz Game")
print("My name is Cameron.")

a = 0

user_name = input("What is your name?")
if user_name == "Ayuka" or user_name == "Maya":
    print("That is a lovely name.")
else:
    print("Your name is alright, I guess.")

time_slept = int(input("How many hours did you sleep last night?"))
if time_slept < 6:
    print("Damn, you need more sleep.")
elif time_slept > 6:
    print("Good for you.")

school_end = input("What time does school end on Tuesday?")
if school_end == "3:05" or school_end == "3:05 pm":
    print("Correct")
    a += 1
else:
    print("Incorrect")

programming = input("How long is programming class on Friday?")
if programming == "45":
    print("Correct")
    a += 1
else:
    print("Incorrect")

canada = input("What is the name of the country north of the U.S.?")
if canada == "Canada":
    print("Correct")
    a += 1
else:
    print("Incorrect")

superbowl = input("What team won the Superbowl last year?")
if superbowl == "Tampa Bay Buccaneers" or superbowl == "Tampa Bay" or superbowl == "Buccaneers":
    print("Correct")
    a += 1
else:
    print("Incorrect")

white_dude = input("Who was the first president of the U.S.?")
if white_dude == "George Washington":
    print("Correct")
    a += 1
else:
    print("Incorrect")

if a == 1:
    print("You scored 20%")
elif a == 2:
    print("You scored 40%")
elif a == 3:
    print("You scored 60%")
elif a == 4:
    print("You scored 80%")
elif a == 5:
    print("You scored 100%")





