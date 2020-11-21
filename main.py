from flask import Flask,render_template,url_for,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Buyer.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xda\x96+\xccN\xadB3\xbf\x8d\x11>\xdd\x0fhn'
db = SQLAlchemy(app)

#--------------DATABASE-------------------------

User = []

Products = [
    {
        "name" : "Sony XT",
        "description" : "Take a look at Sony Xperia TX detailed specifications and features. Product Features: Single Sim, 3G, Wi-Fi, HDMI, NFC. Dual Core, 1.5 GHz Processor.",
        "price" : 20000
    },
    {
        "name" : "Nepali Oblong",
        "description" : "The commercial cultivation of this variety takes place in India with its roots in Assam. This lemon variety has a smooth and glossy texture with medium acidity and very few or no seeds.",
        "price" : 250
    },
    {
        "name" : "Pusa Sadabahar",
        "description" : "Another variety by Indian Agricultural Research Institute, introduced in 2004. This cultivar produces higher yields of tomatoes.The fruits are oval in shape and have a shiny skin with a bright red color.",
        "price" : 150
    }
]

Cart = [
    {
        "name" : "Sony XT",
        "description" : "Take a look at Sony Xperia TX detailed specifications and features. Product Features: Single Sim, 3G, Wi-Fi, HDMI, NFC. Dual Core, 1.5 GHz Processor.",
        "price" : 20000,
        "image": "Sony.jpg"
    },
    {
        "name" : "Pusa Sadabahar",
        "description" : "Another variety by Indian Agricultural Research Institute, introduced in 2004. This cultivar produces higher yields of tomatoes.The fruits are oval in shape and have a shiny skin with a bright red color.",
        "price" : 150
    }
]

#--------------DATABASE-------------------------

#---------------ROUTES--------------------------
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("home.html" , prod = Products)

@app.route("/customerSignIn" ,methods=["POST", "GET"])
def customerSignIn():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "user@gmail.com" and password == "password":
            if "remember-me" in request.form:
                session["email"] = email
                session["password"] = password
                flash("Login Sucessfull", "sucess")
                return redirect(url_for("home"))
            else:
                session["email"] = email
                flash("Login Sucessfull", "sucess")
                return redirect(url_for("home")) 
        else:
            flash("Email or password is incorrect", "error")
            return redirect(url_for("customerSignIn"))
    return render_template("CustomerSignIn.html")

@app.route("/customerSignUp",methods=['POST', 'GET'])
def customerSignUp():
    return render_template("CustomerSignUp.html")

@app.route("/sellerSignIn",methods=['POST', 'GET'])
def sellerSignIn():
    return render_template("SellerSignIn.html")

@app.route("/sellerSignIn",methods=['POST', 'GET'])
def sellerSignUp():
    return render_template("SellerSignIn.html")

#CREATE_ACCOUNT
@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        if "sign-in" in request.form:
            return redirect(url_for("login"))
        else:
            if not request.form["email"] or not request.form["password"]:
                flash("Please Enter all required fields", "error")
                return redirect(url_for("create_account"))
            else:
               email = request.form["email"]
               password = request.form["password"]
               session["email"] = email
               session["password"] = password
               flash("Account sucessfully Created", "success")
               return redirect(url_for("home")) 
    else:
        return render_template("create_account.html")

#CART
@app.route("/cart", methods=["GET", "POST"])
def cart():
    return render_template("Cart.html", c=Cart)

#ERROR HANDLING
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


#---------------ROUTES--------------------------

if __name__ == '__main__':
    app.run(debug=True)
