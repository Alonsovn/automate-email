import datetime

import pandas as pd
import yagmail

from src.newsFeed import NewsFeed


def send_email():
    df = pd.read_excel("people.xlsx")
    date_from = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    date_to = datetime.datetime.now().strftime("%Y-%m-%d")

    for index, row in df.iterrows():
        news_feed = NewsFeed(interest=row['interest'], date_from=date_from,
                             date_to=date_to)
        email = yagmail.SMTP(user="alonsonh94@gmail.com",
                             password="fluidrnjqkpktrvt")
        email.send(to=row['email'],
                   subject=f"Your {row['interest']} news for today!",
                   contents=f"Hi {row['name']}\n See what's on about {row['interest']} today."
                            f"\n {news_feed.get()} \nRegards")
