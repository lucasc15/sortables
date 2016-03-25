import os
import json

class match():

    """A class for matching listings to a product object with loaded products.
    Searches for the best product given a list of product listings with
    1 json entry per line"""

    def __init__(self, products, listingF='listings.txt', subDir = 'data'):

        path = os.path.join( os.getcwd(), subDir )

        self.products = products
        self.listings = os.path.join( path, listingF )
        self.results = {}

    def pipeline(self):
        f = open(self.listings, 'r')

        for line in f:
            tmp = json.loads(line.lower())

            manufacturer = tmp['manufacturer'].split()
            title = tmp['title'].split()

            for m in manufacturer:
                #match manufacturers from listing to product
                if self.products.searchManufacturer(m):
                    product_name = self.products.searchTitle(m, title)
                    if product_name:
                        try:
                            self.results[product_name] += [tmp]
                        except KeyError:
                            self.results[product_name] = [tmp]

    def outputResults(self, outputF = 'results.txt', subDir = 'results'):
        res = ""

        for product_name in self.results:
            res += '{"product_name": "' + product_name + '", '
            res += '"listings": ['
            res += ', '.join( [ json.dumps(i) for i in self.results[product_name] ] ) + ']}\n'

        fname = os.path.join( os.path.join( os.getcwd(), subDir ), outputF )
        f = open(fname, 'w')
        f.write(res)
        f.close()