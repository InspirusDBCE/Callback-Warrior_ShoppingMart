from flask import Flask,render_template,url_for,request,session,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Buyer.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phoneNo = db.Column(db.Integer(), nullable=False)
    pinCode = db.Column(db.Integer(), nullable=False)

    def __init__(self, email, password , address, phoneNo, pinCode):
        self.email = email
        self.password = password
        self.address = address
        self.phoneNo = phoneNo
        self.pinCode = pinCode

#ROUTES
@app.route('/')
def home():
    return render_template("home.html")

#LOGIN
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if "new-account" in request.form:
            return redirect(url_for("create_account")) 
        email = request.form["email"]
        password = request.form["password"]
        foundUser = Buyer.query.filter_by(email=email, password=password).first()
        if foundUser:
            if "remember-me" in request.form:
                session["email"] = email
                session["password"] = password
                return redirect(url_for("home"))
            else:
                return redirect(url_for("home")) 
        else:
            flash("Email or password is incorrect", "error")
    else:
        return render_template("Login.html")

#CREATE_ACCOUNT
@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        if "sign-in" in request.form:
            return redirect(url_for("login"))
        else:
            if not request.form["name"] or not request.form["email"] or not request.form["password"]:
                flash("Please Enter all required fields", "error")
            else:
                name = request.form["name"]
                email = request.form["email"]
                passowrd = request.form["password"]
                Buyer = Buyers(name, email, passowrd)
                db.session.add(Buyer)
                db.session.commit()
                flash("Account sucessfully Created", "success")
                return redirect(url_for("home"))
    else:
        return render_template("create_account.html")

#ERROR HANDLING
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)