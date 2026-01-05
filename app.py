from flask import Flask, render_template, request

app = Flask(__name__)

students = []  # Temporary in-memory storage

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-student', methods=['POST'])
def add_student():
    name = request.form['name']
    marks = request.form['marks']
    students.append({'name': name, 'marks': marks})
    return f"Student {name} added with marks {marks}!<br><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)

