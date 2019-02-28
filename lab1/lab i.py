# EXERCISE 1 - SIMPLE MATH
# Write a program that asks you for two numbers (interactively), sums the numbers, and prints the result on
# screen.

def exercise1():

    print("Sum Generator")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print("The sum of your two numbers is ", (num1 + num2))

exercise1()


# EXERCISE 2 - STRING EXPERIMENT
# Given a string, return a string made of the first two and the last two chars of the original string.
# If a string is shorter than two characters, return the empty string.

def exercise2():

    string = input("Enter a word: ")
    finalString = ""

    if (len(string) < 2):
        print(finalString)
    else:
        finalString += string[:2]
        finalString += string[-2:]
        print(finalString)

exercise2()


# EXERCISE 3 - TO-DO LIST
# Given a list of tasks, implement a todo_manager program to perform four actions:
# Insert a new task (a string of text)
# Remove a task (by typing its content, exactly)
# Show all existing tasks
# Close the program
# At startup, the program shows a menu with the 4 options, and for each choice, performs the requested action.
# After the action (except action 4), the program returns to the prompt for actions.

def exercise3():

    action = 0
    tasks = []

    print("Welcome to todo_manager!")

    while (action != 4):
        print("\nType the number corresponding to the action you wish to perform:")

        print("1. Insert a new task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Close the program")

        action = int(input("Your choice: "))

        if (action == 1):
            tasks.append(input("Type the task you would like to insert: "))
        elif (action == 2):
            tasks.remove(input("Type the task you would like to remove: "))
        elif (action == 3):
            for each in tasks:
                print(each)
        elif (action > 4):
            print("Invalid action")
            action = int(input("Your choice: "))

    print("Thank you for using todo_manager!")

exercise3()