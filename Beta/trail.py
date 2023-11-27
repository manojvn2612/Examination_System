from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        question = request.form['question']
        type = request.form['type']
        options = request.form.getlist('options')

        # Validate the form data
        if not question or not type or len(options) < 2:
            return render_template('set_paper.html', error='Please fill in all the required fields.')

        # Save the form data to the database
        # ...

        # Redirect to the success page
        return redirect(url_for('success'))

    else:
        return render_template('set_paper.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
