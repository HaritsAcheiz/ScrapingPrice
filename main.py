"""
This program will get price of an item that you want to know.
"""
import iPrice

if __name__ == '__main__':
    list_price = iPrice.getPrice('apple-iphone-13-mini')
    print(list_price.title)
    print(list_price.description)
    list_price.run()