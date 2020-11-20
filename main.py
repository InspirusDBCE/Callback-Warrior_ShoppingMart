from flask import Flask,render_template,url_for,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Buyer.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xda\x96+\xccN\xadB3\xbf\x8d\x11>\xdd\x0fhn'
db = SQLAlchemy(app)

#--------------DATABASE-------------------------
class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phoneNo = db.Column(db.Integer(), nullable=False)
    pinCode = db.Column(db.Integer(), nullable=False)
    CART = db.relationship("Cart")


    def __init__(self,name, email, password , address, phoneNo, pinCode):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.phoneNo = phoneNo
        self.pinCode = pinCode

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phoneNo = db.Column(db.Integer(), nullable=False)
    companyName = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, name, email, password , address, phoneNo):
        self.name = name 
        self.email = email
        self.password = password
        self.address = address
        self.phoneNo = phoneNo

class Cart (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False,default='default.jpg')
    price = db.Column(db.Integer(), nullable=False, default=0)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'),nullable=False)

    def __init__(self,name,image,price):
        self.name = name
        self.image = image
        self.price = price

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    image = db.Column(db.String(120), nullable=False,default='default.jpg')
    price = db.Column(db.Integer(), nullable=False, default=0)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self,name,image,price,description):
        self.name = name
        self.image = image
        self.price = price
        self.description = description
    
    def __repr__(self):
        return '<image %r>' % self.image


#--------------DATABASE-------------------------

#---------------ROUTES--------------------------
@app.route('/', methods=['POST', 'GET'])
def home():
    product = Products.query.all()
    if request.method == "GET":
        if "search-bar" in request.form:
            search = request.form["search-item"]
            print(f"\n {search} \n")
        if "cart-button" in request.form:
            return redirect(url_for("cart"))
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
                flash("Login Sucessfull", "sucess")
                return redirect(url_for("home"))
            else:
                flash("Login Sucessfull", "sucess")
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
            if not request.form["name"] or not request.form["email"] or not request.form["password"] or not request.form["phoneNo"] or not request.form["address"] or not request.form["pincode"]:
                flash("Please Enter all required fields", "error")
                return redirect(url_for("create_account"))
            else:
                name = request.form["name"]
                email = request.form["email"]
                passowrd = request.form["password"]
                phoneNo = request.form["phoneNo"] 
                address = request.form["address"]
                pincode = request.form["pincode"]
                buyers = Buyer(name, email, passowrd, address, phoneNo,pincode)
                db.session.add(buyers)
                db.session.commit()
                flash("Account sucessfully Created", "success")
                return redirect(url_for("home"))
    else:
        return render_template("create_account.html")

@app.route("/cart")
def cart():
    return render_template("Cart.html")

#ERROR HANDLING
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


#---------------ROUTES--------------------------

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
