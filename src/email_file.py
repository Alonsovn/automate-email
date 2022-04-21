import pandas as pd
import yagmail

from src.newsFeed import NewsFeed

df = pd.read_excel("../people.xlsx")
date_from = "2022-03-20"
date_to = "2022-04-20"

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], date_from=date_from,
                         date_to=date_to)
    email = yagmail.SMTP(user="alonsonh94@gmail.com",
                         password="pwd")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today."
                        f"\n {news_feed.get()} \nRegards")
