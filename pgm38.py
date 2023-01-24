class Publisher:
    def __init__(self,pub_name):
        self.pub_name =pub_name
    def display(self):
        print("Publisher :", self.pub_name)

class Book(Publisher):
    def __init__(self,pub_name):
        Publisher.__init__(self,pub_name)

    def bookdetails(self):
        self.title= input("Book Name :")
        self.author = input("Book Author :")

    def display(self):
        print("Title :", self.title)
        print("Authur :", self.author)

class Python(Book):
    def __init__(self,pub_name):
        Book.__init__(self,pub_name)

    def moredetails(self):
        self.__price = int(input("Book Price :"))
        self.__pages = int(input("Book Pages :"))

    def display(self):
        print("Publisher :",self.pub_name)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.__price)
        print("Pages :",self.__pages)

obj = Python("DC BOOKS")
obj.bookdetails()
obj.moredetails()
print("-----------------------")
obj.display()