import os
from dotenv import load_dotenv
import datetime
from utils.requester import get_data

load_dotenv()
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

API_KEY = os.getenv(f"NEWS_API_KEY")

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

PARAMETERS = {
    "q" : "tesla",
    "from":yesterday,
    "to":today,
    "sortBy":"popularity",
    "apiKey": API_KEY,
}

def check_latest_news():
    data = get_data(url="https://newsapi.org/v2/everything?",params= PARAMETERS)

    most_famous_article = data["articles"][0]
    author = most_famous_article["author"]
    title = most_famous_article["title"]
    description = most_famous_article["description"]

    article_data = {
        "author":author,
        "title":title,
        "description":description,
    }

    return article_data

