# NewsApi key: be59b26e45d2472da851b555881647ac
import requests


class NewsFeed:
    base_url = "https://newsapi.org/v2/everything?"
    API_KEY = "be59b26e45d2472da851b555881647ac"

    def __init__(self, interest, date_from, date_to, language= "en"):
        self.interest = interest
        self.date_from = date_from
        self.date_to = date_to
        self.language = language

    def get(self):
        response = requests.get(
            f'{self.base_url}qInTitle={self.interest}&'
            f'from={self.date_from}&to={self.date_to}&'
            f'language={self.language}&'
            f'apiKey={self.API_KEY}')

        content = response.json()
        articles = content["articles"]

        email_body = ""
        for article in articles:
            email_body += f" {article['title']}, \n {article['url']}\n\n"

        return email_body
