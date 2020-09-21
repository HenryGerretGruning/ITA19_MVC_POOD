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
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        for item in items:
            df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()}, ignore_index=True)
        print(df)