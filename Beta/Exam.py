from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    pnr = 0  # Initialize pnr to None
    if request.method == 'POST':
        # Process the form data
        name = request.form.get('name')
        pnr = request.form.get('pnr')
        return redirect(f'/Dashboard/{pnr}')
    return render_template('login.html', pnr=pnr)  # Pass pnr to the template

@app.route("/register", methods=["POST", "GET"])
def register():
    pnr = None  # Initialize pnr to None
    if request.method == 'POST':
        # Process the form data
        username = request.form.get('username')
        pnr = request.form.get('pnr')
        return redirect(f'/Dashboard/{pnr}')
    return render_template('reg.html', pnr=pnr)  # Pass pnr to the template

@app.route("/Dashboard/<int:pnr>", methods=["POST", "GET"])
def dashboard(pnr):
    return render_template('Dashboard.html', pnr=pnr)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
