from bs4 import BeautifulSoup
import requests
import psycopg2

conn = psycopg2.connect('postgres://rdtjzllcharamn:fd70085c8f469bdd17438cd924f95ce76744959756508b69196cd6be67b7b142@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/de3c8rlvki5aep', sslmode='require')
conn.autocommit = True

c = conn.cursor()

def new(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, "html.parser")
    con = soup.select('div.c-entry-content')
    for c in con:
        all = c.select_one('p').text
        return all

id = 1


html_text = requests.get('https://www.theverge.com/').text
soup = BeautifulSoup(html_text, "html.parser")

posts = soup.select('.c-compact-river__entry')

# print(len(posts))


for post in posts:
    title = post.select_one('.c-entry-box--compact__title').text.strip()
    link = post.select_one('a')
    link = str(link['href'])
    content = new(link)


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



