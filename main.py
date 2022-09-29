"""
This program will get price of an item that you want to know.
"""
import iPrice


if __name__ == '__main__':
    # prices = getPrice('samsung-galaxy-a10')
    prices = iPrice.getPrice()
    prices.infoPrice('samsung-galaxy-a10')
    prices.toFile('test/samsung galaxy a10.csv')
    # keys = getKey('samsung')
    # prices.infoKey()