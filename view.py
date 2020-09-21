class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")
