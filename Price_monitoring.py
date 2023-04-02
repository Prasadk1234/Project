"""import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.google.com/finance/markets/gainers?hl=en')
soup = BeautifulSoup(res.text,'html.parser')

stocks_listing = list(soup.find_all('div', {'class':'T4LgNb'}))

stocks = []

for stock in stocks_listing:
    name = stock.find('div', {'class':'rzR5Id'}).text
    price = stock.find('span', {'class':'JLPHhb'}).text
    gain = stock.find('span', {'class':'NydbP nZQ6l'}).text
    stocks.append({'name': name, 'price': price, 'gain': gain})
    
pprint.pprint(stocks)
"""

import requests
from bs4 import BeautifulSoup
import pprint

def google(stocks):
    res = requests.get('https://www.google.com/finance/markets/gainers?hl=en')
    soup = BeautifulSoup(res.text, 'html.parser')

    stocks_container = soup.find('div', {'class': 'Sy70mc'})
    stocks_listing = stocks_container.find('ul', {'class': 'sbnBtf'})

    stocks = []

    for stock in stocks_listing.find_all('li'):
        name = stock.find('div', {'class': 'COaKTb'}).text
        price = stock.find('div', {'class': 'YMlKec'}).text.strip('₹')
        price = price.replace(',', '')
        float_price = float(price)
        gain = stock.find('span', {'class': 'P2Luy Ez2Ioe'}).text
        if float_price > 500:
            stocks.append({'name': name, 'price': price, 'gain': gain})

stocks = []
pprint.pprint(google(stocks))



#pprint.pprint(soup.find('ul', {'class':'sbnBtf'}).text)

#stocks_listing = soup.find_all('ul', {'class':'sbnBtf'})
#print(stocks_listing)







