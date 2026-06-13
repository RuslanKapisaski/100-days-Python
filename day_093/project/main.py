import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://books.toscrape.com/"


def scrape_books():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    articles = soup.select("article.product_pod")

    for article in articles:
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text
        rating = article.p["class"][1]
        availability = article.select_one(".availability").text.strip()

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return books


def save_to_csv(books):
    df = pd.DataFrame(books)
    df.to_csv("books.csv", index=False)
    print("Data saved to books.csv")


def main():
    print("Scraping books...")
    books = scrape_books()
    save_to_csv(books)
    print(f"Scraped {len(books)} books successfully.")


if __name__ == "__main__":
    main()
