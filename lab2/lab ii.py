# EXERCISE 1 - TO-DO LIST
# Given a list of tasks, implement a todo_manager program to perform four actions:
# Insert a new task (a string of text)
# Remove a task (by typing its content, exactly)
# Show all existing tasks, sorted in alphabetical order
# Close the program
# At startup, the program shows a menu with the 4 options, and for each choice, performs the requested action.
# After the action (except action 4), the program returns to the prompt for actions.

def exercise1():

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
            try:
                tasks.remove(input("Type the task you would like to remove: ") + "\n")
            except:
                print("Item is not in to-do list")
        elif (action == 3):
            for each in sorted(tasks):
                print(each)
        elif (action > 4):
            print("Invalid action")
            action = int(input("Your choice: "))

    print("Thank you for using todo_manager!")

exercise1()


# EXERCISE 2 - TO-DO LIST SAVED FILE
# Extend the program developed in the previous exercise to save and retrieve the list of tasks to/from a text file.
# At startup, the program takes the list of tasks from the file and saves the changes to the file as soon as the user
# decides to close the program.

def exercise2():

    file = open("task_list.txt", "r")
    tasks = file.readlines()
    file.close()

    action = 0
    print("Welcome to todo_manager!")

    while (action != 4):
        print("\nType the number corresponding to the action you wish to perform:")

        print("1. Insert a new task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Close the program")

        action = int(input("Your choice: "))

        if (action == 1):
            tasks.append(input("Type the task you would like to insert: ") + "\n")
        elif (action == 2):
            try:
                tasks.remove(input("Type the task you would like to remove: ") + "\n")
            except:
                print("Item is not in to-do list")
        elif (action == 3):
            print("")                   # formatting
            for each in sorted(tasks):
                print(each[:-1])
        elif (action > 4):
            print("Invalid action")
            action = int(input("Your choice: "))

    modifiedFile = open("task_list.txt", "w")
    modifiedFile.writelines(tasks)
    modifiedFile.close()

    print("\nThank you for using todo_manager!")

exercise2()


# EXERCISE 3 - TASKS DELETION EXTENSION
# Modify the program developed in the previous exercise to remove all the tasks that contain a specific substring.

def exercise3():

    file = open("task_list.txt", "r")
    tasks = file.readlines()
    file.close()

    action = 0
    print("Welcome to todo_manager!")

    while (action != 4):

        print("\nType the number corresponding to the action you wish to perform:")

        print("1. Insert a new task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Close the program")

        action = int(input("Your choice: "))

        if (action == 1):
            tasks.append(input("Type the task you would like to insert: ") + "\n")

        elif (action == 2):
            substring = input("Type the task you would like to remove: ")
            index = 0
            while index < tasks.__len__():
                if tasks[index].find(substring) != -1:
                    tasks.remove(tasks[index])
                else:
                    index += 1

        elif (action == 3):
            print("")                   # formatting
            for each in sorted(tasks):
                print(each[:-1])

        elif (action > 4):
            print("Invalid action")
            action = int(input("Your choice: "))

    modifiedFile = open("task_list.txt", "w")
    modifiedFile.writelines(tasks)
    modifiedFile.close()

    print("\nThank you for using todo_manager!")

exercise3()


# EXERCISE 4 - FIND URGENT TASKS - DICTIONARIES
# Given a "2D dictionary" of tasks, return a new dictionary (using the same 2D format) that contains only the urgent
# tasks and combine them in a single new dictionary.

def exercise4():

    # entries in the dictionary
    tasks = {'todo': 'call John for AmI project organization', 'urgent': True,
             'todo': 'buy a new mouse', 'urgent': True,
             'todo': 'find a present for Angelina\'s birthday', 'urgent': False,
             'todo': 'organize mega party (last week of April)', 'urgent': False,
             'todo': 'book summer holidays', 'urgent': False,
             'todo': 'whatsapp Mary for a coffee', 'urgent': False}

    # an empty dictionary for storing urgent tasks
    urgent_tasks = {}

    for each in tasks:
        if tasks[each]['urgent'] == True:
            urgent_tasks[each] = tasks[each]

    print(urgent_tasks)

exercise4()