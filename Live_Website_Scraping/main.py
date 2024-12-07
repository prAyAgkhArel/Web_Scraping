import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []
for tag in article_tags:
    text = tag.get_text()
    link = tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_votedtxt = article_texts[article_upvotes.index(max(article_upvotes))]
highest_votedlink = article_links[article_upvotes.index(max(article_upvotes))]

print(highest_votedtxt, highest_votedlink)