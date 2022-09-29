from bs4 import BeautifulSoup
import requests
import json
import os
import pandas as pd


class IPrice:
    def __init__(self, title, description, filename):
        self.title = title
        self.description = description
        self.result = {"title": "", "content": [], "status": ""}
        self.scheme = "https"
        self.filename = filename
        # self.pagination = pagination
        self.host = "iprice.co.id"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    def extract_key(self):
        self.extract_key()

    def info_key(self):
        self.extract_key()
        self.view_key()

    def extract_price(self):
        self.extract_price()

    def info_price(self, term):
        self.extract_price(term)
        self.view_price()




class GetKey(IPrice):
    def __init__(self, term):
        super(GetKey, self).__init__(title='Search Key Generator',
                                     description='To check keyword for getPrice',
                                     filename='search')  # Constructor

    def extract_key(self):
        try:
            with requests.Session() as session:
                content = session.get(f'{self.scheme}://{self.host}/{self.filename}/?term={self.term}',
                                      headers=self.headers)
        except:
            content = 'invalid format'

        if content.status_code == 200:
            soup = BeautifulSoup(content.text, "html.parser")
            result = soup.findAll('div', {'class': 'mb3-xs-4x pu kA oT vs vt vn vJ mb3-xs-4x vK'})
        else:
            result = content.status_code

        return result

    def view_key(self):
        pass

class GetPrice(IPrice):
    # Constructor
    def __init__(self):
        super(GetPrice, self).__init__(
            title = 'Product Price Comparison',
            description = 'To check price for any item in many market place',
            filename = 'harga')

    # Function to extract price
    def extract_price(self, term):
        try:
            with requests.Session() as session:
                content = session.get(f'{self.scheme}://{self.host}/{self.filename}/{term}/', headers=self.headers)
        except Exception:
            content = 'invalid format'
        if content != 'invalid format':
            if content.status_code == 200:
                soup = BeautifulSoup(content.text, "html.parser")
                self.result['title'] = soup.find('h1').text
                soup = soup.find('div', {'class': 'default-offers'})
                products = soup.findAll('div', {'class': 'r2 oU I'})
                for i in products:
                    dictofcontent = {"product": "", "price": "", "link": ""}
                    dictofcontent['product'] = i.find('p', {'class': "oz b R e3"}).text
                    dictofcontent['price'] = i.find('div', {'class': 'vb f24 b gM c2'}).text
                    dictofcontent['link'] = 'iprice.co.id' + i.find('a', href=True)['href']
                    self.result['content'].append(dictofcontent)
                self.result['status'] = "Succeed"
            else:
                self.result['status'] = str(content.status_code)

        else:
            self.result['status'] = content

        return self.result

    def view_price(self):
        for i in self.result:
            try:
                for j in range(len(self.result[i])):
                    print('\n')
                    for k in self.result[i][j]:
                        print(f"{k} : {self.result[i][j][k]}")
            except:
                print(f"{i} : {self.result[i]}")

    def to_file(self, filepath):
        ext = filepath.split('.')[1]
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        if ext == 'json':
            with open(filepath, "w+") as f:
                json.dump(self.result['content'], f)
        if ext == 'csv':
            df = pd.DataFrame(self.result['content'])
            df.to_csv(filepath, index=False)
        if ext == 'excel':
            df = pd.DataFrame(self.result['content'])
            df.to_excel(filepath, index=False)
