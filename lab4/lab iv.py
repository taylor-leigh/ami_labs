# EXERCISE 2 - TELEGRAM BOT WITH DATABASE
#  Modify the Telegram bot developed in the previous lab by replacing the text file with the database.
# The bot should accept the same commands of the previous version.

import pymysql.cursors
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.message.reply_text('Hello! This is AmITaskListBot.'
                              'You can use one of the following commands:'
                              '\n1. /showTasks\n2. /newTask\n3. /removeTask'
                              '\n4. /removeAllTasks')


def echo(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text =
                     "I'm sorry, I can't do that.")


def getConnection():
    connection = pymysql.connect(host = 'localhost', user = 'root', password = 'root',
                    db = 'todolist', charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor)
    return connection


# displays all tasks
def showTasks(bot, update):

    tasks_to_show = []

    sql = "SELECT todo FROM task;"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)

        for each in cursor:
            tasks_to_show.append(each['todo'])

    finally:
        conn.close()

    if len(tasks_to_show) == 0:
        bot.send_message(chat_id = update.message.chat_id, text = "Nothing to do here!")
    else:
        bot.send_message(chat_id = update.message.chat_id, text = sorted(tasks_to_show))


# adds a new task to the list
def newTask(bot, update, args):

    new_task = ' '.join(args)

    sql = "INSERT INTO task (todo) VALUE (%s);"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, new_task)
        conn.commit()
        bot.send_message(chat_id=update.message.chat_id, text=
        "The new task was successfully added to the list!")

    except IOError:
        bot.send_message(chat_id = update.message.chat_id, text =
        'Unable to add task.')

    finally:
        conn.close()


# removes a specific task from the list
def removeTask(bot, update, args):

    remove = ' '.join(args)

    sql = "DELETE FROM task WHERE todo = %s;"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, remove)
        conn.commit()
        bot.send_message(chat_id = update.message.chat_id, text =
                         "The task was successfully deleted!")

    except IOError:
        bot.send_message(chat_id = update.message.chat_id, text =
                         "The task you specified is not in the list.")

    finally:
        conn.close()


# removes all tasks containing a specific substring from the list
def removeAllTasks(bot, update, args):

    substring = '%' + ' '.join(args) + '%'
    removed_tasks = []

    sql_find = "SELECT todo FROM task WHERE todo LIKE %s;"   # finds each task that contains the substring
    sql_remove = "DELETE FROM task WHERE todo LIKE %s;" # deletes each task that contains the substring

    conn = getConnection()

    try:
        cursor = conn.cursor()
        cursor.execute(sql_find, substring)

        # adds items in the cursor to the list of removed tasks
        for each in cursor:
            removed_tasks.append(each['todo'])

        if len(removed_tasks) != 0:
            # removes elements from the database
            cursor.execute(sql_remove, substring)
            conn.commit()

            bot.send_message(chat_id = update.message.chat_id, text =
                         "The elements " + ', '.join(removed_tasks) +
                         " were successfully removed!")
        else:
            bot.send_message(chat_id=update.message.chat_id, text =
            "No tasks to delete!")

    except IOError:
        bot.send_message(chat_id = update.message.chat_id, text =
        "Unable to delete tasks.")

    finally:
        conn.close()


if __name__ == '__main__':

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