from flask import Flask, session, redirect, url_for, request, render_template
from datetime import timedelta

# Initializes the Flask application.
app = Flask(__name__)

# secret key to secure the session data
app.secret_key = 'abscsecretkey' 

app.permanent_session_lifetime =  timedelta(seconds=60)

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if  request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            session.permanent = True
            session['user'] = username
            return redirect(url_for('dashboard'))
        return "Invalid credentials, please try again."
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = session['user']
        return render_template('dashboard.html', user= user)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


# This function is executed before every request.
@app.before_request
def make_session_permanent():
    session.permanent   = True
    # session.modified    = True


if __name__ == '__main__':
    app.run(debug=True)