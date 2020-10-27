class Pair(object):
    def __init__(self,val1 = 0, val2 = 0):
        self.__val1 = val1
        self.__val2 = val2

    def __str__(self):
        return f"Value 1: {self.__val1}, Value 2: {self.__val2}"

    def __add__(self,other):
        res1 = self.__val1 + other.__val1
        res2 = self.__val2 + other.__val2
        return Pair(res1,res2)