class Book :
    #intiated constractor 
    def __init__(self,title,quantity,author,price):
          self.title = title
          self.quantity = quantity
          self.author = author
          self.price = price
# create objects 
book1 = Book('book 1','author 1',120)
book2 = Book('book 2','author 2',220)
book3 = Book('book 3','author 3',320)

print(book1)
print(book2)
print(book3)
