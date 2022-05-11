from bs4 import BeautifulSoup
import requests
import os
import psycopg2
import sqlite3

def tech():
    #creating database and if already exists connecting to it
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.autocommit = True

    # conn = sqlite3.connect('new.db')
    c = conn.cursor()


    #for creating a table
    try:
        c.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT, link TEXT)''')

    except: 
        pass


    html_text = requests.get('https://techcrunch.com').text
    soup = BeautifulSoup(html_text, "html.parser")

    posts = soup.select('.post-block.post-block--image.post-block--unread')


    for post in posts:
        title = post.select_one('a.post-block__title__link').text.strip()
        content = post.select_one('div.post-block__content').text.strip()
        link = post.select_one('a.post-block__title__link')
        link = str(link['href'])
    
        
        # print(title, content)
        # print(link['href'])

        c.execute('''INSERT OR IGNORE INTO POSTS(TITLE, CONTENT, LINK)VALUES(?,?,?)''', (title, content, link))

    conn.commit()
    conn.close()

tech()