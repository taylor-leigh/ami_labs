# Functions for interacting with the todolist database

import pymysql.cursors

def getConnection():
    connection = pymysql.connect(host = 'localhost', user = 'root', password = 'root',
                    db = 'todolist', charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor)
    return connection


def getTasks():

    sql = "SELECT * FROM task;"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql)

        tasks_to_display = cursor.fetchall()

    finally:
        conn.close()

    return tasks_to_display


def addTask(input):

    sql = "INSERT INTO task (todo) VALUE (%s);"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, input)
        conn.commit()

    finally:
        conn.close()


def removeTask(input):

    sql = "DELETE FROM task WHERE id = %s;"

    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, input)
        conn.commit()

    finally:
        conn.close()
