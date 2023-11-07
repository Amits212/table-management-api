from flask import Flask, render_template, request, session
import socket

app = Flask(__name__)
app.secret_key = 'roi312313'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'fname' not in session:
        session['fname'] = []
    if 'filepath' not in session:
        session['filepath'] = []

    if request.method == 'POST':
        fname = request.form['fname']
        filepath = request.form['filepath']
        session['fname'].append(fname)
        session['filepath'].append(filepath)
        return render_template("home.html", fname=session['fname'], filepath=session['filepath'])
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
