from flask import Flask, render_template, redirect, request, url_for,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#secret key is

app.config['SECRET_KEY'] ="Examination"
#adding Database
#app.config['SQLALCHEMY_DATABASE_URI']
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["GET", "POST"])
def login():
    pnr = 0
    if request.method == 'POST':
        name = request.form.get('name')
        pnr = request.form.get('pnr')
        session["pnr"] = pnr
        return redirect("/Dashboard")
    else:
        return render_template('login.html')
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        fname ,Mname, Lname = name.split(" ")
        pnr = request.form.get('pnr')
        session["pnr"] = pnr
        return redirect('Dashboard')
    return render_template('reg.html', pnr=pnr)
@app.route("/Dashboard", methods=["POST", "GET"])
def dashboard():
    if "pnr" in session:
        return render_template('Dashboard.html')
    else:
        return redirect(url_for("login"))
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug=True)
