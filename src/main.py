from src.newsFeed import NewsFeed


def main():
    interest = "tesla"
    date_from = "2022-03-20"
    date_to = "2022-04-20"
    language = "en"

    n = NewsFeed(interest, date_from, date_to, language)
    print(n.get())


main()
