import requests
from bs4 import BeautifulSoup

def get_current_bitcoin_price():

    page = requests.get("https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD")

    if page.status_code == 200:

        print("Successfully retrieved web page")

    else:

        print("Error")

    soup = BeautifulSoup(page.content, 'html.parser')

    container = soup.find('span', {"data-reactid":'14'})
    if container:
        print(container.text)

        return container.text

