from api.stock_api import check_stock
from api.news_api import check_latest_news
from api.twilio_api import send_sms


percentage_change = check_stock()

if percentage_change != 0:
    article_data = check_latest_news()
    body = {
        "change": percentage_change,
        "article_data": article_data
    }
    send_sms(body)



