class CashRegister(object):
    Reg_counter = 0
    total_price = 0
    total_wtax = 0
    
    def __init__(self,tax):
        self.__tax = tax

    def add_item(self,price,is_tax):
        CashRegister.Reg_counter += 1
        CashRegister.total_price += price
        if is_tax:
            CashRegister.total_wtax += price + price*self.__tax/100
        else:
            CashRegister.total_wtax += price
        
    def get_count(self):
        return CashRegister.Reg_counter

    def get_total(self):
        return CashRegister.total_price

    def get_total_with_tax(self):
        return round(CashRegister.total_wtax,4)

    def clear(self):
        CashRegister.Reg_counter = 0
        CashRegister.total_price = 0
        CashRegister.total_wtax = 0
    
    def __str__(self):
        return f"Items: {CashRegister.Reg_counter}, total price: {CashRegister.total_price:.2f}, including tax: {CashRegister.total_wtax:.2f}"

