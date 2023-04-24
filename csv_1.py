import requests
from bs4 import BeautifulSoup

def parse_ssr():
    response = requests.get('https://www.kivano.kg/mobilnye-telefony')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('a', {'href':'/product/view/sotovyy-telefon-samsung-galaxy-s23-ultra-12-512gb-zelenyy'}).text
    return data

def parse_crs():
    response = requests.get('https://www.kivano.kg/mobilnye-telefony')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('a', {'href':'/product/view/sotovyy-telefon-samsung-galaxy-s23-ultra-12-512gb-zelenyy'}).text
    return data

if __name__ == '__main__':
    print('Dogecoint rate:',parse_ssr())






