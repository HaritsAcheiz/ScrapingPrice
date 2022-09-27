from bs4 import BeautifulSoup
import requests

class iPrice:
    def __init__(self,item,description):
        self.title = 'Product Price Comparison'
        self.description = description
        self.result = {"title": "", "content": [], "status": ""}
        self.url = "https://iprice.co.id"
        self.item = item
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}

    def extract(self):
        pass

    def viev(self):
        pass

    def run(self):
        self.extract()
        self.view()

class getPrice (iPrice):
    def __init__(self,item):
        super(getPrice,self).__init__(item,'To check price for any item in many market place')

    def extract(self):
        try:
            PAGE = f"harga/{self.item}/"
            with requests.Session() as session:
                content = session.get(f'{self.url}/{PAGE}', headers=self.headers)
        except Exception:
            content = 'invalid format'
        if content != 'invalid format':
            if content.status_code == 200:
                soup = BeautifulSoup(content.text, "html.parser")
                self.result['title'] = soup.find('title').text
                soup = soup.find('div', {'class': 'default-offers'})
                products = soup.findAll('div', {'class': 'r2 oU I'})
                for i in products:
                    dictOfContent = {"product": "", "price": "", "link": ""}
                    dictOfContent['product'] = i.find('p', {'class': "oz b R e3"}).text
                    dictOfContent['price'] = i.find('div', {'class': 'vb f24 b gM c2'}).text
                    dictOfContent['link'] = 'iprice.co.id' + i.find('a', href=True)['href']
                    self.result['content'].append(dictOfContent)
                self.result['status'] = "Succeed"
            else:
                self.result['status'] = content.status_code

        else:
            self.result['status'] = content

        return self.result

    def view(self):
        print(self.result['title'])
        for i in self.result['content']:
            print(i)
        print(self.result['status'])


if __name__ == '__main__':
    list_price = getPrice('samsung-galaxy-a10')
    print(list_price.title)
    print(list_price.description)
    list_price.run()