import email
from flask import Flask, render_template, redirect, request, url_for,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#secret key is

app.config['SECRET_KEY'] ="Examination"
#adding Database

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ramanath%402612@localhost/examination"

db = SQLAlchemy(app)
class Login_Users_s(db.Model):
    __tablename__ = 'Login_student'
    email = db.Column(db.String(32),primary_key = True)
    password = db.Column(db.String(32), primary_key = True)
    def __init__(self,email,password):
        self.email = email
        self.password = password
        
class Login_Users_t(db.Model):
    __tablename__ = 'Login_Teacher'
    email = db.Column(db.String(32),primary_key = True)
    password = db.Column(db.String(32), primary_key = True)
    def __init__(self,email,password):
        self.email = email
        self.password = password
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["GET", "POST"])
def login():
    pnr = None
    if request.method == 'POST':
        email = request.form.get('email')
        pnr = request.form.get('pnr')
        session["pnr"] = pnr
        if Login_Users_s.query.filter_by(email=email).first():
            return redirect("/Dashboard")
        elif Login_Users_t.query.filter_by(email=email).first():
            return redirect("/Dashboard")
        return redirect("/register")
    else:
        return render_template('login.html')
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        pnr = request.form.get('pnr')
        session["pnr"] = pnr
        return redirect("/Dashboard")
    else:
        return render_template('reg.html')
@app.route("/Dashboard", methods=["POST", "GET"])
def dashboard():
    if "pnr" in session:
        pnr = session.get('pnr')
        return render_template('Dashboard.html',pnr = pnr)
    else:
        return redirect(url_for("login"))
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
