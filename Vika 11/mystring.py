class MyString(object):
    def __init__(self,words):
        self.words = words
    
    def __sub__(self,other):
        return abs(len(self.words) - len(other.words))

    def __gt__(self,other):
        return len(self.words) > len(other.words)