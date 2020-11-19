from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world"

@app.route('/login')
def login():
    return render_template('Login.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)