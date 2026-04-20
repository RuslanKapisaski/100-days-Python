import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

website = requests.get(URL)
soup = BeautifulSoup(website.content, "html.parser")

movies_headings = soup.find_all(name="h3",class_="title")

greatest_100_movies =[]
for movie in movies_headings:
    greatest_100_movies.append(movie.text)

greatest_100_movies = list(reversed(greatest_100_movies))

with open("movies.txt", "w") as file:
    for movie in greatest_100_movies:
        file.write(f"{movie}\n")


