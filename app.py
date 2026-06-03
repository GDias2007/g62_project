from flask import Flask, render_template, request, session
from datafile import filename
from classes.bank import Bank
from classes.branch import Branch
from classes.card import Card
from classes.customer import Customer
from classes.transaction import Transaction
from classes.userlogin import Userlogin
from subs.apps_gform import apps_gform
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Bank.read(filename + 'Bancos.db')
Branch.read(filename + 'Bancos.db')
Card.read(filename + 'Bancos.db')
Customer.read(filename + 'Bancos.db')
Transaction.read(filename + 'Bancos.db')
Userlogin.read(filename + 'business.db')

app.secret_key = 'g62_secret_key'

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/login")
def login():
    return render_template("login.html", user="", password="", ulogin=session.get("user"), resul="")

@app.route("/logoff")
def logoff():
    session.pop("user", None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post", "get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password=password, ulogin=session.get("user"), resul=resul)

@app.route("/gform/<cname>", methods=["post", "get"])
def gform(cname):
    return apps_gform(cname)

@app.route("/Userlogin", methods=["post", "get"])
def userlogin():
    return apps_userlogin()

@app.route("/analytics")
def analytics():
    from analytics import gerar_graficos
    ulogin = session.get("user")
    if ulogin is None:
        return render_template("index.html", ulogin=ulogin)
    estatisticas = gerar_graficos()
    return render_template("analytics.html", ulogin=ulogin, estatisticas=estatisticas)

if __name__ == '__main__':
    app.run(debug=True)
