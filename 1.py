from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.theverge.com/tech/').text
soup = BeautifulSoup(html_text, "html.parser")
# print(soup)

posts = soup.select('div.flex.items-center h2')
for post in posts:
    try:
        title = post.select_one('a').text
        link = post.select_one('a')
        link = str(link['href'])
        link = "https://www.theverge.com" + link
        
        print(link)
    except:
        pass


print(len(posts))
# print(posts[0:5])
