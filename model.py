import helpers

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
    # remove item
    def deleteItem(self, name):
        helpers.deleteItem(name)

    # show items
    def showItems(self):
        return helpers.showItems()

    # show item
    def showItem(self, name):
        return helpers.showItem(name)

