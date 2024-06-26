from flask import Flask, redirect, request, render_template, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

def is_authenticated():
    return 'email' in session

@app.before_request
def require_authentication():
    if request.endpoint == 'protected' and not is_authenticated():
        return redirect('/')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login.html')
def safe():
    return render_template('login.html')

@app.route('/injection.html')
def injection():
    return render_template('injection.html')

@app.route('/protected')
def protected():
    if not is_authenticated():
        return redirect('/')
    return render_template('protected.html')

@app.route('/invalid')
def invalid():
    return render_template('invalid.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

# Login w Prepared Statements
@app.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    email = json['email']
    password = json['password']

    query = "SELECT * FROM users WHERE email=? AND password=?"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(query, (email, password))

    data = cursor.fetchone()

    if data:
        session['email'] = email
        return redirect('/protected')
    else:
        return redirect('/invalid')

# Login w/o Prepared Statements
@app.route('/injection', methods=['POST'])
def inj():
    json = request.get_json()
    email = json['email']
    password = json['password']

    query = "SELECT * FROM users WHERE email='%s' AND password='%s'" % (email, password)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(query)

    data = cursor.fetchone()

    if data:
        session['email'] = email
        return redirect('/protected')
    else:
        return redirect('/invalid')

if __name__ == '__main__':
    app.run()
