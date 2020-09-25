import exceptions
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")
    # delete item
    def deleteItem(self, name):
        try:
            self.model.deleteItem(name)
            self.view.deleteItem(name)

        except:
            print("Failed to remove item.")

    def showItems(self):
        items = self.model.showItems()
        self.view.showItems(items)

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def deleteAll(self):
        try:
            self.model.deleteAll()
            print("Sending to view")
            self.view.deleteAll()
        except:
            self.view.noItemsError()

    def updateItem(self, name, price, amount):
        try:
            self.model.updateItem(name, price, amount)
            self.view.updateItem(name)
        except:
            self.view.noItemsError(name)