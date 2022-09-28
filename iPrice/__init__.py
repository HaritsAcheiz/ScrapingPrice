from bs4 import BeautifulSoup
import requests

class iPrice:
    def __init__(self,title,description,term):
        self.title = title
        self.description = description
        self.result = {"title": "", "content": [], "status": ""}
        self.scheme = "https"
        self.host = "iprice.co.id"
        self.filename = "/search/"
        self.term = term
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    def extract(self):
        print('under construction')

    def view(self):
        print('under construction')

    def qgen(self):
        self.qgen()

    def run(self):
        self.extract()
        self.view()



class getKey(iPrice):
    def __init__(self,term):
        super(getKey,self).__init__('Search Key Generator','To check key name for searching item',term) #Constructor

    def qgen(self):
        try:
            with requests.Session() as session:
                content = session.get(f'{self.scheme}://{self.host}{self.filename}?term={self.term}', headers=self.headers)
        except:
            content = 'invalid format'

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, "html.parser")
            result = soup
        else:
            result = content.status_code

        return result

class getPrice (iPrice):
    def __init__(self,term):
        super(getPrice,self).__init__('\nProduct Price Comparison','To check price for any item in many market place',term) #Constructor

    def extract(self):
        try:
            with requests.Session() as session:
                content = session.get(f'{self.scheme}://{self.host}/harga/{self.term}', headers=self.headers)
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
        for i in self.result:
            print(f"\n{i} : ")
            try:
                for j in range(len(self.result[i])):
                    print("\n")
                    for k in self.result[i][j]:
                        print(f"{k} : {self.result[i][j][k]}")
            except:
                print(f"{i} : {self.result[i]}")


if __name__ == '__main__':
    # list_price = getPrice('samsung-galaxy-a10')
    # list_price.run()
    list_key = getKey('samsung')
    # print(list_key.title)
    # print(list_key.description)
    list_key = list_key.qgen()
    print(list_key)
    # result = getKey.qgen()

    # print(f'hasil adalah {result}')