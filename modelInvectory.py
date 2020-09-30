import helpersInvectory

class ModelInvectory:
    # get Invectory data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def addItem(self, name, price, amount):
        helpersInvectory.addItem(name, price, amount)
    # remove item
    def deleteItem(self, name):
        helpersInvectory.deleteItem(name)

    # show items
    def showItems(self):
        return helpersInvectory.showItems()

    # show item
    def showItem(self, name):
        return helpersInvectory.showItem(name)

    def deleteAll(self):
        helpersInvectory.deleteAll()

    def updateItem(self, name, price, amount):
        helpersInvectory.updateItem(name, price, amount)


