from flask import Flask,render_template,url_for,request,session,redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    print("Logging in")
    if request.method == "POST":
        if "new-account" in request.form:
            print("New account")
            return redirect(url_for("create_account")) 
        elif "remember-me" in request.form:
            session["email"] = request.form["email"]
            session["password"] = request.form["password"]
            return redirect(url_for("home"))
        else:
            return redirect(url_for("home")) 
    else:
        return render_template("Login.html")

@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        if "sign-in" in request.form:
            return redirect(url_for("login"))
        else:
            name = request.form["name"]
            email = request.form["email"]
            passowrd = request.form["password"]
            return redirect(url_for("home"))
    else:
        return render_template("create_account.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)