import pandas as pd

class View:
    # show items
    def showItems(self, items):
        #print("Shop items")
        #print("============================")
        #print("name\t|\tprice\t|\tamount")
        #for item in items:
            #print(item.getName()+"\t|\t"+
                  #str(item.getPrice())+"\t\t|\t"+
                  #str(item.getAmount()))
            #print("---------------------------")
        #print("============================")
        print("============================")
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        for item in items:
            df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()}, ignore_index=True)
        print(df)
        print("============================")

    def showItem(self, item):
        print("============================")
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()}, ignore_index=True)
        print(df)
        print("============================")

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop do does not contain {}".format(name))
        print("============================")

    def noItemsError(self):
        print("============================")
        print("List already empty!!!".format())
        print("============================")

    def deleteItem(self, name):
        print("============================")
        print("{} deleted.".format(name))
        print("============================")

    def deleteAll(self):
        print("============================")
        print("All elements were deleted.")
        print("============================")

    def updateItem(self,name):
        print("============================")
        print("Updated {}".format(name))
        print("============================")