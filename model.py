import helpers
import helpersInvectory

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def restock(self, name, price, amount):
        helpers.addItem(name, price, amount)
        helpersInvectory.moveItem(name, price, amount)
    # remove item
    def deleteItem(self, name):
        helpers.deleteItem(name)

    # show items
    def showItems(self):
        return helpers.showItems()

    # show item
    def showItem(self, name):
        return helpers.showItem(name)

    def deleteAll(self):
        helpers.deleteAll()

    def updateItem(self, name, price, amount):
        helpers.updateItem(name, price, amount)
        helpersInvectory.moveItem(name, price, amount)

