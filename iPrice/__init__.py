from bs4 import BeautifulSoup
import requests


def search():
    properties = {"item":"","browser":""}
    properties['item'] = "apple-iphone-13-mini"
    # properties['item'] = input('What are you looking for? :')
    # properties['browser'] = input('What browser are use? :')
    return properties

def extract(input):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'
        }
        HOST = "https://iprice.co.id"
        PAGE = f"harga/{input['item']}/"
        with requests.Session() as session:
            content = session.get(f'{HOST}/{PAGE}', headers=headers)
    except Exception:
        content = None
    result = {"title": "", "produtcs": "", "prices": "", "status": ""}
    if content == None:
        result.status = "Failed"
    else:
        soup = BeautifulSoup(content.text,"html.parser")
        result['title'] = soup.find('title').text
        # for a in soup.find_all('div', attrs={'class': 'N'}):
        #     product = a.find('span', attrs={'class': 'truncate-2 db webkit-box-ns oz kH oV h2-ns g ht b uD'})
        #     result.products.append(product.text) if product != None else False
        #     price = a.find('div', attrs={'class': 'a- db ue iR'})
        #     result.prices.append(price.text) if product != None else False
        # for a in soup.find_all('div', attrs={'class': 'N'}):
        #     product = a.find('span', attrs={'class': 'truncate-2 db webkit-box-ns oz kH oV h2-ns g ht b uD'})
        #     result['products'].append(product.text) if product != None else False
        #     price = a.find('div', attrs={'class': 'a- db ue iR'})
        #     result['prices'].append(price.text) if product != None else False
        result['status'] = "Succeed"

    return result

def view(result):
    print(result)