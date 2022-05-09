from flask import Flask, render_template
import sqlite3
import time
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('new.db')
    c = conn.cursor()
    # c.execute('SELECT title FROM posts')
    # titles = c.fetchall()
    # titles = [str(val[0]) for val in titles]

    # c.execute('SELECT content FROM posts')
    # contents = c.fetchall()
    # contents = [str(val[0]) for val in contents]

    # c.execute('SELECT link FROM posts')
    # links = c.fetchall()
    # links = [str(val[0]) for val in links]

    c.execute('SELECT * FROM posts')
    titles = c.fetchall()
    return render_template('index.html', titles = titles)
    #return data[0]
