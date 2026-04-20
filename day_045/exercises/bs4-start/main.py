from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article in articles:
    link_tag = article.find("a")

    article_text = link_tag.getText()
    article_texts.append(article_text)

    article_link = link_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
best_upvote = max(article_upvotes)
index_of_best_upvote = article_upvotes.index(best_upvote)

best_article ={
    "Name": article_texts[index_of_best_upvote],
    "Link": article_links[index_of_best_upvote],
    "Upvotes": article_upvotes[index_of_best_upvote],
}

print("Best article:")
for entry in best_article.items():
    print(entry)







# with open("website.html", "r") as file:
#     website_content = file.read()
#
# soup = BeautifulSoup(website_content, "lxml") # Object that allows to tap in various parts of the site

#print(soup.title)
#print(soup.title.string)
#print(soup.title.name)
#print(soup.prettify())

# Find all method
# a_anchor_tags = soup.find_all(name="a")
# print(a_anchor_tags)
#
# for tag in a_anchor_tags:
#     print(tag.get("href"))
#

# heading = soup.find(name="h1")
# print(heading.text)

# section_heading=soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.text)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)









