from flask import Flask
app = Flask(__name__)


@app.route('/home')
def hello_world():
    return 'Hello, World!'

@app.route("/login")
def login_page():
    return "./login.html"


if __name__ == '__main__':
    app.run()