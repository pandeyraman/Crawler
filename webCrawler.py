from bs4 import BeautifulSoup
from urllib import request

def trade_spider(max_pages):
    page =1
    while page < max_pages:
        url = "http://www.addic7ed.com/shows.php#LetterT"
        source_code = request.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a',{'class':'version'}):
            td = link.get('td')
            title = link.string
            print(td)
            print(title)
    page += 1

trade_spider(1)

