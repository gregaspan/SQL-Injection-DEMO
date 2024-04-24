import sqlite3

def seed_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT,
                       password TEXT)''')

    cursor.execute("SELECT * FROM users WHERE email=?", ('email',))
    data = cursor.fetchone()

    if data is None:
        default_email = 'email'
        default_password = 'password'

        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                       (default_email, default_password))

        conn.commit()

    conn.close()

seed_database()
