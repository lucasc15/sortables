import json
import os

class products():
    """Class to store product information in a dictionary of
    dictionaries for product information. Reads in data from
    a txt file with 1 JSON entry per line."""

    def __init__(self, fileName, subDir = 'data'):
        self.data = {}
        path = os.path.join( os.path.join(os.getcwd(), subDir), fileName)
        self.f = open(path, 'r')
        self.load()

    def load(self):
        for line in self.f:
            tmp = json.loads(line.lower())

            manufacturer = tmp['manufacturer']
            try:
                family = tmp['family']
            except KeyError:
                family = ''
            model = tmp['model']
            name = tmp['product_name']

            if manufacturer not in self.data:
                self.data[manufacturer] = {}
            if family not in self.data[manufacturer]:
                self.data[manufacturer][family] = {}
            else:
                self.data[manufacturer][family][model] = name

    def searchManufacturer(self, m):
        if m in self.data:
            return True
        else:
            return False

    def searchTitle(self, m, title):
        for family in title:
            if family in self.data[m]:
                for model in title:
                    if model in self.data[m][family]:
                        return self.data[m][family][model]
        return False
