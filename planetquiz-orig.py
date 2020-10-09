"""
Solar System Quiz 2020
By Roch Derilo
"""
# Define variables
name = ""
score = 0

while name == "":
    name_input = input("What is your name? ")
    name = str(name_input.title())
else:
    print("Welcome to Solar System Quiz 2020, " + name + ". Let's get started!")


# Questions
questions = {
"red planet" : "mars",
"closest star to us" : "sun",
"planet closest to the sun" : "mercury",
"largest planet" : "jupiter",
"planet with beautiful rings" : "saturn",
"planet full of methane" : "uranus",
"twin planet of Uranus" : "neptune",
"planet with recently discovered phosphine gas" : "venus",
"dwarf planet that was once thought of as a planet" : "pluto",
"only planet with confirmed life" : "earth"        
}

# Iterate through the dictionary
for item in questions:
    print("Question: What is the " + item + "?")
    answer = input()
    answer = answer.lower()
    if answer == questions[item]:
        print("Your answer is correct!")
        score = score + 1
    else:
        print("Your answer is incorrect.")
        
# End score
if score >= 7 :
    print("Congratulations, " + name + "!. You got " + str(score) + " out of 10.\nYou passed the quiz!")
else:
    print("Unfortunately, " + name + ", you only got " + str(score) + " out of 10.\nYou failed the quiz.")
    
# Ending
print("\n\nThanks for taking the Solar System quiz. See you next time!")
