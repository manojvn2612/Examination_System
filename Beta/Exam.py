
from re import A
from click import option
from flask import Flask, render_template, redirect, request, url_for,session,jsonify
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
    #classroom = db.Column(db.String(32))
    def __init__(self,email,password):
        self.email = email
        self.password = password
        
class Login_Users_t(db.Model):
    __tablename__ = 'Login_Teacher'
    email = db.Column(db.String(32),primary_key = True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(32), nullable=False)
    #designation = db.Column(db.String(32))
    def __init__(self,email,password):
        self.email = email
        self.password = password
class Questions(db.Model):
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
     
@app.route("/set_paper", methods=["POST", "GET"])
def set_paper():
    session = db.session
    last_q = text("SELECT last_q()")
    get_id = session.execute(last_q).fetchone()
    paper_id_details = get_id[0] + 1
    return render_template('set_paper.html')
@app.route("/submit-paper", methods=['POST'])
def test_submitted():
    session = db.session
    data = request.json.get('responses',[])
    # Process the data as needed
    print(data)
    for question_id, question_data in data.items():
        question_text = question_data['question']
        options = question_data['options']
        
            # Extracting option values
        # Extracting option values
        option_a = options['a']['text']
        option_b = options['b']['text']
        option_c = options['c']['text']
        option_d = options['d']['text']
        
        # Checking which option is selected
        if options['a']['selected']:
            correct_option = 'a'
        elif options['b']['selected']:
            correct_option = 'b'
        elif options['c']['selected']:
            correct_option = 'c'
        elif options['d']['selected']:
            correct_option = 'd'
        else:
            correct_option = None  # Handle the case where no option is selected

            # Inserting into the database
        
        print(option_a, option_b, option_c,option_d,correct_option)
        last_q = text("SELECT last_q()")
        get_id = session.execute(last_q).fetchone()
        paper_id_details = get_id[0] + 1
        create_table = text(f"CALL q_p_create({paper_id_details})")
        db.session.execute(create_table)
        qid = 1
        query = text(
        f"INSERT INTO questions.q{paper_id_details} (question_text,option_a,option_b,option_c,option_d,correct) VALUES ('{question_text}', '{option_a}','{option_b}', '{option_c}','{option_d}','{correct_option}')"
        )
        qid += 1
                # Add the new question to the database
        db.session.execute(query)

            # Commit changes to the database
        db.session.commit()

    # Return a response if necessary
    return redirect(url_for("dashboard"))

@app.route("/show_paper", methods=["GET", "POST"])
def show_paper():
    return render_template("show_paper.html")
@app.route("/logout")
def logout():
    return "<h1>Logout</h1>"
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
