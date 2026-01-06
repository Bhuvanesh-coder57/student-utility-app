from flask import Flask, render_template, request

import sqlite3
from database import init_db

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-student', methods=['POST'])
def add_student():
    name = request.form['name']
    marks = request.form['marks']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    conn.close()
    return f"Student {name} saved permanently!<br><a href='/'>Go back</a>"


@app.route("/students")
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, marks FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template("students.html", students=students)


    
if __name__ == '__main__':
    app.run(debug=True)

