
from flask import Flask, render_template, redirect, request, url_for,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
app = Flask(__name__)

#secret key is

app.config['SECRET_KEY'] ="Examination"
#adding Database

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Ramanath%402612@localhost/examination"



app.config['SQLALCHEMY_BINDS'] = {
    'questions': 'mysql+pymysql://root:Ramanath%402612@localhost/questions'
}
db = SQLAlchemy(app)
class Login_Users_s(db.Model):
    __tablename__ = 'Login_student'
    email = db.Column(db.String(32),primary_key = True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(32), nullable=False)
    def __init__(self,email,password):
        self.email = email
        self.password = password
        
class Login_Users_t(db.Model):
    __tablename__ = 'Login_Teacher'
    email = db.Column(db.String(32),primary_key = True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(32), nullable=False)
    def __init__(self,email,password):
        self.email = email
        self.password = password
class Question_Paper(db.Model):
    __tablename__ = 'Question_Paper'
    qid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    qgid = db.Column(db.Integer, nullable=False)
    Teacher = db.Column(db.String(32), nullable=False)
    DOC = db.Column(db.DateTime, default=datetime.utcnow)
    DOS = db.Column(db.DateTime)
    DOE = db.Column(db.DateTime)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        designation = request.form.get('designation')
        session["email"] = email
        session["designation"] = designation
        if designation == "Student" and Login_Users_s.query.filter_by(email=email,password = password).first():
            print(designation)
            return redirect("/Dashboard")
        elif designation == "Teacher" and Login_Users_t.query.filter_by(email=email,password = password).first():
            return redirect("/Dashboard")
        return redirect("/register")
    else:
        return render_template('login.html')
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        session["email"] = email
        return redirect("/Dashboard")
    else:
        return render_template('reg.html')
@app.route("/Dashboard", methods=["POST", "GET"])
def dashboard():
    if "email" and "designation" in session:
        email = session.get('email')
        designation = session.get('designation')
        if designation == "Teacher":
            return render_template('Dashboard_teacher.html',email = email)
        else:
            return render_template("Dashboard_student.html",email = email)
    else:
        return redirect(url_for("login"))
    return 
@app.route("/set_paper", methods=["POST", "GET"])
def set_paper():
    try:
        session = db.session
        last_q = text("SELECT last_q() as last_qid")
        get_id = session.execute(last_q).fetchone()
        paper_id_details = get_id[0]+1
        call_procedure = text("CALL q_p_create(:paper_id)")
        session.execute(call_procedure, {'paper_id': paper_id})
        session.commit()
        return render_template('set_paper.html',q_id = paper_id_details)
    except Exception as e:
        return f"Error: {str(e)}", 500
@app.errorhandler(500)
def wrong(error):
    return  render_template('500.html'),500
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.create_all()
    app.run(debug=True)
