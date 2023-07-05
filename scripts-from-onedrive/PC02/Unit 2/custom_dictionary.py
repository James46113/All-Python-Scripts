from random import choice

class Dictionary:
    author = "James"
    
    def __init__(self, str1, str2, str3, str4, str5):
        self.list_strings = [str1, str2, str3, str4, str5]
        
    def add_item(self, item):
        self.list_strings += item
        
    def item(self, index: int):
        return self.list_strings[index]
    
    def rand_word(self):
        return choice(self.list_strings)
    
    def get_length(self):
        return len(self.list_strings)
    
    def output(self):
        print(self.list_strings)
    
    @staticmethod
    def output_class_information():
        print(Dictionary.author)
        print(vars(Dictionary))
        
        
a = Dictionary("a", "b", "c", "d", "e")
a.add_item("f")
a.add_item("g")
a.add_item("h")
print(a.list_strings)
print(a.item(1))
print(a.rand_word())
print(a.get_length())
a.output()
