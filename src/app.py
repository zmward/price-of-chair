__author__ = 'Zach'

import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print(price)
else:
    print("Your chair costs {} too much!".format(abs(price - 200)))
