"""
Question Manager for Solar System Quiz 2020
This program allows users to view, add, edit, and delete questions
used in the Solar System Quiz.

By Roch Derilo

"""

# Reading the questions from questions.csv
questions = {}
file = open("questions.csv", "r")  
text = file.readlines() 
for row in text:
    cols = row.split(",")
    questions[cols[0]] = cols[1].strip()
file.close()

print("Welcome to Question Manager\n")
options = {
"1" : "view the questions",
"2" : "add a question",
"3" : "edit a question",
"4" : "delete a question",
"5" : "save your changes",
"0" : "exit this program",
}

answer = ""
while answer != "0" :
    
    print("What do you want to do?")
    for num in options :
        print("Press " + num + " to " + options[num])
    answer = input("Enter your choice: ")
    if answer in options :
        print("You chose to " + options[answer] + ".\n")
    
    if answer == "1" :
        print("Here are the questions:")
        i = 0
        for item in questions :
            i = i + 1
            print(str(i) + ". What is the " + item + "? (Answer: " + questions[item] + ")")
        input("Press enter to continue...\n")
    
    if answer == "2" :
        print("Enter a new question:")
        new_question = input("What is the... ")
        new_answer = input("Enter the answer: ")
        questions[new_question] = new_answer
        print("\nYou added the following question:")
        print("'What is the " + new_question + "?'")
        print("\nwith the following answer:")
        print("'" + new_answer + "'")
        input("Press enter to continue...\n")
    
    if answer == "3" :
        print("Which question do you want to edit?")
        num = input("Enter a number from 1 to " + str(len(questions)) + ": ")
        i = 0
        for item in questions :
            i = i + 1
            if str(i) == num:
                print("You chose to edit the following question:")
                print(str(i) + ". What is the " + item + "? (Answer: " + questions[item] + ")")
                new_answer = input("Enter new answer: ")
                questions[item] = new_answer
                print(str(i) + ". What is the " + item + "? (Answer: " + questions[item] + ")")
        input("Press enter to continue...\n")
    
    if answer == "4" :
        print("Which question do you want to delete?")
        num = input("Enter a number from 1 to " + str(len(questions)) + ": ")
        i = 0
        for item in questions :
            i = i + 1
            if str(i) == num:
                print("You chose to delete the following question:")
                print(str(i) + ". What is the " + item + "? (Answer: " + questions[item] + ")")
                answer = input("Proceed to delete? (Answer YES to delete) ")
                if answer == "YES" :
                    selecteditem = item
                else :
                    selecteditem = ""
        if selecteditem != "" :
            del(questions[selecteditem])
            print("Question has been deleted.")
        else :
            print("\nQuestion was NOT deleted.")
        input("Press enter to continue...\n")
    
    if answer == "5" :
        print("Saving to file...")
        with open("questions.csv", "w") as file:
            for key in questions.keys():
                file.write("%s,%s\n"%(key, questions[key]))
        file.close()
        print("Your changes have been saved to 'questions.csv'.")
        input("Press enter to continue...\n")
    
    if answer == "0" :
        print("Bye.")
