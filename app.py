from flask import Flask, render_template
import sqlite3
import time
import os
import psycopg2
from scripts.database import DATABASE_URL
try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    pass

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app = Flask(__name__)

@app.route('/')
def index():
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

    c.execute('SELECT * FROM TECHCRUNCH ORDER BY ID DESC LIMIT 5')
    techcrunchs = c.fetchall()

    c.execute('SELECT * FROM MASHABLE ORDER BY ID DESC LIMIT 5')
    mashables = c.fetchall()

    c.execute('SELECT * FROM VERGE ORDER BY ID DESC LIMIT 3')
    verges = c.fetchall()

    return render_template('index.html', techcrunchs = techcrunchs, mashables = mashables, verges = verges)
    
    #return data[0]

@app.route('/techcrunch')
def techcrunch():
    c = conn.cursor()
    c.execute('SELECT * FROM TECHCRUNCH ORDER BY ID DESC')
    techcrunchs = c.fetchall()
    return render_template('techcrunch.html', techcrunchs = techcrunchs)



@app.route('/mashable')
def mashable():
    c = conn.cursor()
    c.execute('SELECT * FROM MASHABLE ORDER BY ID DESC')
    mashables = c.fetchall()
    return render_template('mashable.html', mashables = mashables)

@app.route('/verge')
def verge():
    c = conn.cursor()
    c.execute('SELECT * FROM VERGE ORDER BY ID DESC')
    verges = c.fetchall()
    return render_template('verge.html', verges = verges)
