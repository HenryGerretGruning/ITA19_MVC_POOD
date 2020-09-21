# shop.py
class Shop:
    def __init__(self):
        self.products = []

    def __repr__(self):
        description = ""
        for product in self.products:
            description += repr(product)
            description += "\n=================\n"
        return description

    def addProduct(self, product):
        self.products.append(product)