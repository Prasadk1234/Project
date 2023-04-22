import requests
from bs4 import BeautifulSoup
import pprint

def stocks_gainers():
    res = requests.get('https://www.google.com/finance/markets/gainers?hl=en')
    soup = BeautifulSoup(res.text, 'html.parser')
    stocks_container_gainers = soup.find('div', {'class': 'Sy70mc'})
    stocks_listing_gainers = stocks_container_gainers.find('ul', {'class': 'sbnBtf'})
    Gainer= []
    for stock in stocks_listing_gainers.find_all('li'):
        name = stock.find('div', {'class': 'COaKTb'}).text
        price = stock.find('div', {'class': 'YMlKec'}).text
        gain = stock.find('span', {'class': 'P2Luy Ez2Ioe'}).text
        Gainer.append({'name': name, 'price': price, 'gain': gain})
    pprint.pprint(Gainer)


def stocks_loser():
    res1 = requests.get('https://www.google.com/finance/markets/losers?hl=en')
    soup1 = BeautifulSoup(res1.text, 'html.parser')
    Stocks_container_losers = soup1.find('div', {'class': 'Vd323d'})
    stocks_listing_losers = Stocks_container_losers.find('ul', {'class':'sbnBtf'})
    Loser = []
    for stock in stocks_listing_losers.find_all('li'):
        name = stock.find('div', {'class': 'ZvmM7'}).text
        price = stock.find('div', {'class': 'YMlKec'}).text
        Lose = stock.find('span', {'class': 'P2Luy Ebnabc'}).text
        Loser.append({'name': name, 'price': price, 'Lose': Lose})
    pprint.pprint(Loser)

stocks_gainers()

