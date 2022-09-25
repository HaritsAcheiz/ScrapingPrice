"""
This program will get price of an item that you want to know.
"""
import iPrice

if __name__ == '__main__':
    print('Product Price Comparison')
    item = iPrice.search()
    result = iPrice.extract(item)
    iPrice.view(result)