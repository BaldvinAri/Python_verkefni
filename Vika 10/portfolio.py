
class Stock(object):
    def __init__(self,name,val):
        self.stock = f"{name}: {val}"

    def __str__(self):
        return self.stock


class Portfolio(object):
    def __init__(self):
        self.data = ""
        
    def add(self,stock):
        if self.data:
            self.data += "\n" + stock.stock
        else:
            self.data = stock.stock

    def __str__(self):
        return self.data
