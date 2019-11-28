
class Summary():
    def __init__(self,string):
        self.list_word = []
        self.list_word_num = [1] * 50
        self.string = string
    def summary(self):
        string = self.string
        list_word = self.list_word = []
        list_word_num = self.list_word_num
        max = 0
        length_str = len(string)
        for i in range(0, length_str):
            length = 0
            temp_str = string[i]
            j = 0
            number = 0
            #判断队列中是否存在

            for j in range (0,len(list_word)):
                if list_word[j] == temp_str:
                    list_word_num[j] = list_word_num[j] + 1
                    break
                else:
                    length += 1
            if length == len(list_word):
                list_word.append(temp_str)
        self.list_word = list_word
        self.list_word_num = list_word_num
    def get_list_word(self):
        return self.list_word
    def get_list_word_num(self):
        return self.list_word_num
    def set_list_word_num(self,num):
        self.list_word_num = num
    def set_list_word(self,word):
        self.list_word = word
    def Clear(self):
        self.list_word = None
        self.list_word_num = [1] * 50
