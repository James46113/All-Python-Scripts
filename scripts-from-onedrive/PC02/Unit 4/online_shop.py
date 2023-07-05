class Item:
    def __init__(self, ID, title, description):
        self.ID = ID
        self.title = title
        self.description = description
    
    def __str__(self) -> str:
        return self.title + ", " + self.description


class Book(Item):
    def __init__(self, ID, title, description, author, publisher):
        Item.__init__(self, ID, title, description)
        self.author = author
        self.publisher = publisher
        
    def __str__(self) -> str:
        temp = Item.__str__(self)
        return temp + f", {self.author}, {self.publisher}"
        

class Movie(Item):
    def __init__(self, ID, title, description, release_date, director, genre):
        Item.__init__(self, ID, title, description)
        self.release_date = release_date
        self.director = director
        self.genre = genre
        
    def __str__(self) -> str:
        temp = Item.__str__(self)
        return temp + f", {self.release_date}, {self.director}, {self.genre}"


book1 = Book("482", "book1", "A book", "author", "publisher")
shop_list = [Book("482", "book1", "A book", "author", "publisher"), Book("482", "book1", "A book", "author", "publisher"),
             Movie("482", "movie1", "A movie", "2014", "a person", "action"), Movie("482", "movie1", "A movie", "2014", "a person", "action")]
for item in shop_list:
    print(item)
    
# Make a loop where user adds items, until they want to end
