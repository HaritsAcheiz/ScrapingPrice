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
    result = {"title": "", "content": [], "status": ""}
    if content == None:
        result.status = "Failed"
    else:
        soup = BeautifulSoup(content.text,"html.parser")
        result['title'] = soup.find('title').text
        soup = soup.find('div',{'class':'default-offers'})
        products = soup.findAll('div', {'class': 'r2 oU I'})
        for i in products:
            dictOfContent = {"product":"", "price":"", "link":""}
            dictOfContent['product'] = i.find('p',{'class': "oz b R e3"}).text
            dictOfContent['price'] = i.find('div', {'class': 'vb f24 b gM c2'}).text
            dictOfContent['link'] = 'iprice.co.id' + i.find('a', href=True)['href']
            result['content'].append(dictOfContent)
        result['status'] = "Succeed"

    return result

def view(result):
    print(result['title'])
    # print(result['content'])
    for i in result['content']:
        print(i)
    print(result['status'])