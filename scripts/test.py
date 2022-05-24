from bs4 import BeautifulSoup
import requests

def content():
    html_text = requests.get('https://www.theverge.com/').text
    soup = BeautifulSoup(html_text, "html.parser")

    posts = soup.select('.c-compact-river__entry')
    con(posts)

def con(posts):
    for post in posts:
        link = post.select_one('a')
        link = link['href']
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, "html.parser")
        con = soup.select('div.c-entry-content')
        for c in con:
            content = c.select_one('p').text

content()