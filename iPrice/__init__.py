from bs4 import BeautifulSoup
import requests
from selenium import webdriver

def search():
    properties = {"item":"","browser":""}
    properties['item'] = "apple-iphone-13-mini"
    # properties['item'] = input('What are you looking for? :')
    # properties['browser'] = input('What browser are use? :')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0'}
    HOST = "https://iprice.co.id"
    PAGE = f"harga/{properties['item']}/"
    with requests.Session() as session:
        (r := session.get(HOST, headers=headers)).raise_for_status()
        (r := session.get(f'{HOST}/{PAGE}', headers=headers)).raise_for_status()
    print(r)
    return properties

def extract(input):
    try:
        url = f"https://iprice.co.id/harga/{input['item']}/"
        content = requests.get(url)
        result = BeautifulSoup(content)
    except Exception:
        print("Not-Responded")
        content = None
    if content == None:
        result = "Failed"
    else:
        result = content.text

    return result

def view(result):
    print(result)