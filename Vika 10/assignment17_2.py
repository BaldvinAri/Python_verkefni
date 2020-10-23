class Sentence(object):
    def __init__(self,sent):
        self.sent = sent

    def get_first_word(self):
        return self.sent.split()[0]

    def get_all_words(self):
        return self.sent.split()

    def replace(self,index,new_word):
        if index in range(len(self.sent.split())):
            sent_list = self.sent.split()
            sent_list[index] = new_word
            self.sent = " ".join(sent_list)
    
    def __str__(self):
        return self.sent



