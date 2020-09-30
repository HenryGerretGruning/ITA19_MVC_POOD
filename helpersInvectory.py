import exceptions
from product import Product


# repsresents shop structure
# list of Product type objects
itemsInInvectory = []

# add item to items
def addItem(name, price, amount):
    global itemsInInvectory
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in itemsInInvectory:
        raise exceptions.ItemExists("Item {} exists".format(name))
    else:
        itemsInInvectory.append(product)
# delete item
def deleteItem(name):
    global itemsInInvectory
    # control all items step by step
    for item in itemsInInvectory:
        # if the name is the same as we search
        if (item.getName() == name):
            itemsInInvectory.remove(item)


        else:
            continue
            raise exceptions.ItemExists("{} not found!".format(name))

# show items
def showItems():
    global itemsInInvectory
    # control if items exists
    if len(itemsInInvectory) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return itemsInInvectory

# show item
def showItem(name):
    global itemsInInvectory
    # control all items step by step
    for item in itemsInInvectory:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("{} not found!".format(name))

def deleteAll():
    global itemsInInvectory
    if len(itemsInInvectory) > 0:
        itemsInInvectory.clear()
    else:
        raise exceptions.ItemExists("List is empty".format())


def updateItem(name, price, amount):
    global itemsInInvectory

    # control is item already exists
    for item in itemsInInvectory:
        # if the name is the same as we search
        if (item.getName() == name):
            item.price = item.setPrice(price)
            item.amount = item.setAmount(amount)

        else:
            continue
            raise exceptions.ItemExists("{} not found!".format(name))


def moveItem(name, price, amount):
    global itemsInInvectory
    # control all items step by step
    for item in itemsInInvectory:
        # if the name is the same as we search
        if (item.getName() == name):

            amounta = item.getAmount()
            item.amount = item.setAmount(amounta-amount)

        else:
            continue
            raise exceptions.ItemExists("{} not found!".format(name))

