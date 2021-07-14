from re import T
from flask import Flask, redirect, render_template, request, url_for,session,abort
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView


import sqlite3

app=Flask(__name__)
list=[]



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/vaughan/Desktop/coding3/ocean.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

admin = Admin(app)

class ocean(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    insta = db.Column(db.String(30))
    numb = db.Column(db.String(30))
    book = db.Column(db.String(30))
    descript = db.Column(db.String(60))
    price = db.Column(db.String(30))
    oprice = db.Column(db.String(30))

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
         
admin.add_view(SecureModelView(ocean, db.session))

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def ocean():
    return render_template("ocean.html")


@app.route("/login",methods=["GET","POST"])
def login():   

    error = None
    if request.method == "POST":

        if request.method == "POST":

            if request.form['admin'] == 'ACES' and request.form['password'] == 'ACCESS':
                session['logged_in'] = True
                return redirect(url_for('success'), code=307)
            else :
                error = ' Invalid Authorization '
    return render_template("login.html",error=error)


@app.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")


@app.route("/buy")
def buy():
    connection=sqlite3.connect("ocean.db")
    connection.row_factory= sqlite3.Row
    bdata=connection.execute("SELECT * FROM ocean")
    return render_template("buy.html",bdata=bdata)
    

@app.route("/sell")
def sell():
    return render_template("sell.html")

def logout():
    session.clear()
    return redirect("/logout")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/notice" ,methods=["POSt"])
def notice():
    
    name= request.args.get("name")
    surname= request.args.get("surname")
    email=request.args.get("email")
    insta= request.args.get("insta")
    numb= request.args.get("numb")
    book=request.args.get("book")
    descript= request.args.get("descript")
    price=request.args.get("price")
    oprice=request.args.get("oprice")
    X = libofbook(name,surname,email,insta,numb,book,descript,price,oprice)
    
    return render_template("notice.html",X=X)


def libofbook(name,surname,email,insta,numb,book,descript,price,oprice):

    connection=sqlite3.connect("ocean.db")
    connection.execute("INSERT INTO ocean(name,surname,email,insta,numb,book,descript,price,oprice) VALUES (:name,:surname,:email,:insta,:numb,:book,:descript,:price,:oprice)",{"name":name,"surname":surname,"email":email,"insta":insta,"numb":numb,"book":book,"descript":descript,"price":price,"oprice":oprice})
    connection.commit()
    connection.close()
    return (0)


@app.route("/data" , methods=["POST"])
def data():
   
    connection=sqlite3.connect("ocean.db")
    connection.row_factory= sqlite3.Row
    bdata=connection.execute("SELECT * FROM ocean")

    return render_template("data.html",bdata=bdata)
    
    connection.close()

@app.route("/ocean")
def index():
    return render_template("home.html")

@app.route("/success",methods=["get","post"])
def success():
    return render_template("success.html")
    
    
