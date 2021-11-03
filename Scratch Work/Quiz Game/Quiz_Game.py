print("Welcome to the Quiz Game")
print("My name is Cameron.")

print()

number_correct = 0

user_name = input("What is your name?")
if user_name == "Ayuka" or user_name == "Maya":
    print("That is a lovely name.")
else:
    print("Your name is alright, I guess.")

print()

time_slept = int(input("How many hours did you sleep last night?"))
if time_slept < 6:
    print("Damn, you need more sleep.")
elif time_slept > 6:
    print("Good for you.")

print()

school_end = input("What time does school end on Tuesday?")
if school_end == "3:05" or school_end == "3:05 pm":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect")

print()

programming = input("How long is programming class on Friday?")
if programming == "45":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect")

print()

print("Please Capitalize For The Text Answers.")

print()

canada = input("What is the name of the country north of the U.S.?")
if canada == "Canada":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect")

print()

superbowl = input("What team won the Super Bowl last year?")
if superbowl == "Tampa Bay Buccaneers" or superbowl == "Tampa Bay" or superbowl == "Buccaneers" or superbowl == "Bucs":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect")

print()

white_dude = input("Who was the first president of the U.S.?")
if white_dude == "George Washington":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect")

print()

print("Which of the following is true?")
print("a) Seahawks' QB Russell Wilson ruptured a tendon in the game against the Rams")
print("b) Geno Smith is has been backup QB for over 6 years")
print("c) The Seahawks won Super Bowl L")
multiple_choice = input("Type the correct letter.")
if multiple_choice == "a" or multiple_choice == "A":
    print("Correct")
    number_correct += 1
else:
    print("Incorrect, the correct answer is a.")

print()

psycho = input("True or False: Wearing socks to bed is a tendency of a psychopaths.")
if psycho == "True" or psycho == "true":
    print("Good to know that you are sane.")
    number_correct += 1
else:
    print("I am genuinely afraid of you.")

print()

if number_correct == 1:
    print("You scored 14%")
elif number_correct == 2:
    print("You scored 28%")
elif number_correct == 3:
    print("You scored 42%")
elif number_correct == 4:
    print("You scored 57%")
elif number_correct == 5:
    print("You scored 71%")
elif number_correct == 6:
    print("You scored 85%")
elif number_correct == 7:
    print("You scored 100%")

else:
    print("You failed.")

print()

print("Good job.")
