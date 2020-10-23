#class Score goes here

class Score(object):
    def __init__(self,value=0):
        self.value = value

    def add(self,other):
        self.value += other

    def decrease(self,other):
        self.value -= other

    def __str__(self):
        return str(self.value)