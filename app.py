from flask import Flask, render_template, redirect, request

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
    cursor.execute("SELECT id, name, marks FROM students")
    students = cursor.fetchall()

    total_no_students = len(students)

    total_marks = 0

    student_with_grades = []

    for student in students:
        marks = int(student[2])
        total_marks += marks

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        student_with_grades.append((student[0], student[1], marks, grade))

    if total_no_students > 0:
        average = int(total_marks / total_no_students)
    else:
        average = 0

    conn.close()

    return render_template(
        "students.html",
        students=student_with_grades,
        total=total_no_students,
        average=average
    )

   



@app.route("/delete/<int:id>")
def delete_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/students")



if __name__ == '__main__':
    app.run(debug=True)

