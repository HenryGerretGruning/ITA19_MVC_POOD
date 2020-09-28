# ui.py

# import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from view import View
from invectory import Invectory
from modelInvectory import ModelInvectory


# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)

# create shop and invectory and add products to invectory
shop = Controller(Model(Shop()), View())
invectory = Controller(ModelInvectory(Invectory()), View())

invectory.addItem("bread", 0.80, 10)
invectory.addItem("milk", 0.50, 50)
invectory.addItem("wine", 5.60, 5)

#Restocks the shop, emptying the invectory
shop.restock("wine", 5.60, 2)
shop.showItems()


# show items
invectory.showItems()
#shop.showItem("milk")
#shop.deleteItem("milk")




#shop.deleteAll()
#shop.deleteAll()

#shop.updateItem('wine', 0.99, 20)
#shop.showItems()