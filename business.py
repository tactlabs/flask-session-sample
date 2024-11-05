from flask import Flask, session, redirect, url_for, request, render_template
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)

# Configure session to use filesystem

# the session_type is used to store the user data in the file 
app.config['SESSION_TYPE'] = 'filesystem'

# secret key to secure the session data
app.config['SECRET_KEY'] = 'abscsecretkey' 


app.config['SESSION_PERMANENT'] = True 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=10)




# Initialize the session
Session(app)

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            session['user'] = username  # Store user in session
            session.permanent = True  # Mark the session as permanent (this activates the 60-second timeout)
            return redirect(url_for('dashboard'))
        return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = session['user']
        return render_template('dashboard.html', user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
