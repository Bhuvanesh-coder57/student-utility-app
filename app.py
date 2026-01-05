from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return " welcome to my Student Utility App "
@app.route('/about')
def about():
    return "This app helps students manage academic data"


if __name__ == '__main__':
    app.run(debug=True)
