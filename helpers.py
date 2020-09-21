import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items
