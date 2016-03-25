from match import match
from products import products


def main():
    product = products('products.txt')
    matcher = match(product)
    matcher.pipeline()
    matcher.outputResults()

if __name__ == '__main__':
    main()
