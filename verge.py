from bs4 import BeautifulSoup
import requests
import psycopg2
import os
from scripts.database import DATABASE_URL

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    pass

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

c = conn.cursor()

def new(link):
    html_text = requests.get(link).text
    # print(html_text)
    soup = BeautifulSoup(html_text, "html.parser")
    con = soup.select('div.duet--article--article-body-component')
    for c in con:
        all = c.select_one('p').text
        # print(all)
        return all

id = 1


html_text = requests.get('https://www.theverge.com/tech/').text
soup = BeautifulSoup(html_text, "html.parser")
# print(soup)

posts = soup.select('.items-center h2')

# print(len(posts))


for post in posts:
    try:
        title = post.select_one('a').text
        link = post.select_one('a')
        link = str(link['href'])
        link = "https://www.theverge.com/" + link
        content = new(link)
    except:
        pass


    # print(title)
    # print(content)
    # print(link)
    try:
        c.execute('SELECT MAX(ID) AS ID FROM VERGE')
        max_id = c.fetchone()
        max_id = int(max_id[0])
        id = max_id + 1
    except:
        pass
    
    # c.execute('INSERT INTO VERGE(CONTENT) VALUES (%s)', content)
    c.execute('''INSERT INTO VERGE(ID, TITLE, CONTENT, LINK) VALUES (%s, %s, %s, %s) ON CONFLICT (TITLE) DO NOTHING''', (id, title, content, link))

conn.commit()
conn.close()



