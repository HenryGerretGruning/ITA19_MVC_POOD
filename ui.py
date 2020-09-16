# ui.py

# import classes and files
from product import Product
from shop import Shop

# create products
bread = Product("Bread", 0.80, 10)
milk = Product("Milk", 0.50, 50)
wine = Product("Wine", 5.60, 5)

# create shop and add products to shop
shop = Shop()
shop.addProduct(bread)
shop.addProduct(milk)
shop.addProduct(wine)


print(shop)