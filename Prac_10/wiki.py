import wikipedia

search = input("Enter Search Phrase: ")
while search != "":
    print(wikipedia.search(search))
    page_tit = input("Page Title:")
    try:
        page_info = wikipedia.page(page_tit)
        print(page_info.title)
        print(wikipedia.summary(page_tit))
        print(page_info.url)
    except wikipedia.exceptions.DisambiguationError:
        print("Enter Page title or Search Phrase: ")
