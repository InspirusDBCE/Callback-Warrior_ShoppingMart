from flask import Flask,render_template,url_for,request,session,redirect,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xda\x96+\xccN\xadB3\xbf\x8d\x11>\xdd\x0fhn'


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
        "price" : 130
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

@app.route("/sellerSignUp",methods=['POST', 'GET'])
def sellerSignUp():
    return render_template("SellerSignUp.html")

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
