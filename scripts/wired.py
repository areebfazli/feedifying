from bs4 import BeautifulSoup
import requests
import os
import psycopg2

conn = psycopg2.connect('postgres://rdtjzllcharamn:fd70085c8f469bdd17438cd924f95ce76744959756508b69196cd6be67b7b142@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/de3c8rlvki5aep', sslmode='require')
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
        c.execute('SELECT MAX(ID) AS ID FROM WIRED')
        max_id = c.fetchone()
        max_id = int(max_id[0])
        id = max_id + 1
    except:
        pass

    # c.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES (%s,%s,%s) ON CONFLICT (TITLE) DO NOTHING''', (title, content, link))
    c.execute('''INSERT INTO WIRED(ID, TITLE, CONTENT, LINK) VALUES (%s, %s, %s, %s) ON CONFLICT (TITLE) DO NOTHING''', (id, title, content, link))

conn.commit()
conn.close()





