"""
This program will get price of an item that you want to know.
"""
import iPrice
import flask


if __name__ == '__main__':
    # prices = getPrice('samsung-galaxy-a10')
    prices = iPrice.GetPrice()
    prices.info_price('samsung-galaxy-a10')
    # prices.extract_price('samsung-galaxy-a10')
    # prices.to_file('test/samsung galaxy a10.csv')
    # keys = getKey('samsung')
    # prices.infoKey()