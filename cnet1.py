from bs4 import BeautifulSoup
import requests
import os
import psycopg2

def tech():
    #creating database and if already exists connecting to it
    conn = psycopg2.connect('postgres://rdtjzllcharamn:fd70085c8f469bdd17438cd924f95ce76744959756508b69196cd6be67b7b142@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/de3c8rlvki5aep', sslmode='require')
    conn.autocommit = True

    # conn = sqlite3.connect('new.db')
    c = conn.cursor()


    #for creating a table
    # try:
    #     c.execute('''CREATE TABLE posts(ID SERIAL PRIMARY KEY, TITLE VARCHAR UNIQUE, CONTENT VARCHAR, LINK VARCHAR)''')

    # except: 
    #     pass


    html_text = requests.get('https://techcrunch.com').text
    soup = BeautifulSoup(html_text, "html.parser")

    posts = soup.select('.post-block.post-block--image.post-block--unread')
    id = 1

    for post in posts:
        title = post.select_one('a.post-block__title__link').text.strip()
        content = post.select_one('div.post-block__content').text.strip()
        link = post.select_one('a.post-block__title__link')
        link = str(link['href'])
    
        
        # print(title, content)
        # print(link['href'])
        try:
            c.execute('SELECT MAX(ID) AS ID FROM TEST')
            max_id = c.fetchone()
            max_id = int(max_id[0])
            id = max_id + 1
        except:
            pass

        # c.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES (%s,%s,%s) ON CONFLICT (TITLE) DO NOTHING''', (title, content, link))
        c.execute('''INSERT INTO TEST(ID, TITLE, CONTENT, LINK) VALUES (%s, %s, %s, %s) ON CONFLICT (TITLE) DO NOTHING''', (id, title, content, link))

    conn.commit()
    conn.close()

tech()