# EXERCISE - TELEGRAM BOT: TO-DO MANAGER
# Modify the program developed in the third exercise of the previous lab so that a Telegram bot is run at
# startup. Before running the bot, the program should load the task list contained in the file task_list.txt.
# Then, every time the list is changed, the program should save the new list to the file.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text('Hello! This is AmITaskListBot.'
                              'You can use one of the following commands:'
                              '\n1. /showTasks\n2. /newTask\n3. /removeTask'
                              '\n4. /removeAllTasks')


def echo(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text =
                     "I'm sorry, I can't do that.")


# displays all tasks
def showTasks(bot, update):

    if len(tasks) == 0: bot.send_message(chat_id = update.message.chat_id, text = "Nothing to do here!")
    else: bot.send_message(chat_id = update.message.chat_id, text = sorted(tasks))


# adds a new task to the list
def newTask(bot, update, args):

    new_task = ' '.join(args)

    tasks.append(new_task)
    bot.send_message(chat_id = update.message.chat_id, text =
        "The new task was successfully added to the list!")

    # saves changes to the file
    saveChanges()


# removes a specific task from the list
def removeTask(bot, update, args):

    remove = ' '.join(args)

    if remove in tasks:
        tasks.remove(remove)
        bot.send_message(chat_id = update.message.chat_id, text =
                         "The task was successfully deleted!")
    else:
        bot.send_message(chat_id = update.message.chat_id, text =
                         "The task you specified is not in the list.")

    # saves changes to the file
    saveChanges()


# removes all tasks containing a specific substring from the list
def removeAllTasks(bot, update, args):

    substring = ' '.join(args)
    removed_tasks = []

    index = 0
    while index < len(tasks):
        if tasks[index].find(substring) != -1:
            removed_tasks.append(tasks[index])
            tasks.remove(tasks[index])
        else:
            index += 1

    if len(removed_tasks) != 0:
        bot.send_message(chat_id = update.message.chat_id, text =
                     "The elements " + ', '.join(removed_tasks) +
                     " were successfully removed!")
    else:
        bot.send_message(chat_id = update.message.chat_id, text =
                         "No tasks to delete!")

    # saves changes to the file
    saveChanges()


def saveChanges():
    try:
        modified_file = open("task_list.txt", "w")
        for task in tasks:
            modified_file.write(task + "\n")
        modified_file.close()
    except IOError:
        print("Could not save changes")



if __name__ == '__main__':

    tasks = []

    # reads the task list from the file into a python list
    try:
        file = open("task_list.txt", "r")
        tasks = file.read().splitlines()
        file.close()
    except IOError:
        print("File not found")
        exit()

    # bot setup
    updater = Updater(token = '500733589:AAERa4iBMpMZ68XdtK1LsKsQ_d2UrFhTdkQ')

    # handlers for responding to user commands
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))  #starts the bot
    dispatcher.add_handler(MessageHandler(Filters.text, echo))  #handles unknown inputs
    dispatcher.add_handler(CommandHandler('showTasks', showTasks))  #prints the sorted list of tasks
    dispatcher.add_handler(CommandHandler('newTask', newTask, pass_args = True))    #adds a task
    dispatcher.add_handler(CommandHandler('removeTask', removeTask, pass_args = True))  #removes a specific task
    dispatcher.add_handler(CommandHandler('removeAllTasks', removeAllTasks, pass_args = True))  #removes all tasks containing a specific substring

    # starts the bot
    updater.start_polling()
    updater.idle()