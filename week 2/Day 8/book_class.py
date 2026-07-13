class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = int(pages)
        
        
    def display_info(self):
        print(f"""
Title  : {self.title.title()}
Author : {self.author.title()}
Pages  : {self.pages}
""")
        
book1 = Book('Atomic habits','James clear',320)
book2 = Book('the alchemist','paulo coelho',208)

book1.display_info()
book2.display_info()