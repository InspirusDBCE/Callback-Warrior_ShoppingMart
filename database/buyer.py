from flask_sqlalchemy import SQLAlchemy

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phoneNo = db.Column(db.Integer(10), nullable=False)

    def __init__(self, email, password , address, phoneNo):
        self.email = email
        self.password = password
        self.address = address
        self.phoneNo = phoneNo

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phoneNo = db.Column(db.Integer(10), nullable=False)
    companyName = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, email, password , address, phoneNo):
        self.email = email
        self.password = password
        self.address = address
        self.phoneNo = phoneNo

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    image = db.Column(db.String(120), nullable=False,default='default.jpg')
    price = db.Column(db.Interger(10), nullable=False, default=0)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self,name,image,price,description):
        self.name = name
        self.image = image
        self.price = price
        self.description = description
