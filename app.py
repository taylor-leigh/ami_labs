from flask import Flask, render_template, url_for, redirect, request
import db_functions

app = Flask(__name__)


@app.route('/')
def default_page():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    tasklist = db_functions.getTasks()
    return render_template("index.html", tasklist = tasklist)


@app.route('/add', methods = ['POST'])
def add():
    task = request.form['task']
    db_functions.addTask(task)
    return redirect(url_for('index'))


@app.route('/delete/<task>')
def delete(task):
    db_functions.removeTask(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
