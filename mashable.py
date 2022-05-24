from bs4 import BeautifulSoup
import requests
import os
import psycopg2
from scripts.database import DATABASE_URL

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    pass

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

c = conn.cursor()

html_text = requests.get('https://in.mashable.com/article').text
soup = BeautifulSoup(html_text, "html.parser")

posts = soup.select('li.blogroll')
id = 1

for post in posts:
    title = post.select_one('.caption').text.strip()
    content = post.select_one('div.deck').text.strip()
    link = post.select_one('a')
    link = str(link['href'])

    try:
        c.execute('SELECT MAX(ID) AS ID FROM MASHABLE')
        max_id = c.fetchone()
        max_id = int(max_id[0])
        id = max_id + 1
    except:
        pass

    # c.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES (%s,%s,%s) ON CONFLICT (TITLE) DO NOTHING''', (title, content, link))
    c.execute('''INSERT INTO MASHABLE(ID, TITLE, CONTENT, LINK) VALUES (%s, %s, %s, %s) ON CONFLICT (TITLE) DO NOTHING''', (id, title, content, link))

conn.commit()
conn.close()





