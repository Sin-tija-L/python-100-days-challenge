from flask import Flask, request, redirect, render_template, session, flash
from dotenv import load_dotenv
import sqlite3
import os

# Initialize the app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv(dotenv_path='python-dotenv/.env')

# Set the secret key for sessions from environment variable or explicitly
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY', 'fallback-secret-key')

# Database setup
DATABASE = "blog.db"

def init_db():
    """Initialize the database with tables for users and posts."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create the users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    # Create the posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Insert a default user
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password) 
        VALUES ('alisoons', 'alise123')
    """)
    conn.commit()
    conn.close()

# Initialize the database
init_db()

def query_db(query, args=(), one=False, commit=False):
    """Helper function to query the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    if commit:
        conn.commit()
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def create_user(username, password):
    """Helper function to create a new user."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = query_db("SELECT * FROM users WHERE username = ?", (username,), one=True)
        print("Login attempt for:", username)
        print("User from DB:", user)

        if user:
            if user[2] == password:  # Ensure password matches
                session['username'] = username
                print("Session set for:", session['username'])
                flash("Login successful.", "success")
                return redirect('/feed')
            else:
                flash("Invalid password. Please try again.", "error")
        else:
            flash("User does not exist. Please create an account.", "error")
    
    return render_template('login.html')

@app.route('/feed', methods=["GET", "POST"])
def feed():
    if 'username' in session:
        if request.method == "POST":
            new_title = request.form["title"]
            new_content = request.form["content"]
            query_db("INSERT INTO posts (title, content) VALUES (?, ?)", (new_title, new_content), commit=True)
            flash("New blog entry added.", "success")
        
        posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
        return render_template('feed_logged_in.html', posts=posts)
    else:
        posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
        return render_template('feed_not_logged_in.html', posts=posts)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    flash("Logout successful.", "success")
    return redirect('/login')  # Redirect to the /login route

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
