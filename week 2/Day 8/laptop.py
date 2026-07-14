class Laptop:
    def __init__(self,brand,ram,storage):
        self.brand = brand
        self.ram = int(ram)
        self.storage = int(storage)
        
    def display_info(self):
        
        print(f"""
Brand   : {self.brand.title()}
Ram     : {self.ram} GB
Storage : {self.storage} GB
""")
    
    def upgrade_ram(self):
        self.ram += 2
        print(f'ram upgraded, now ram is {self.ram} GB')
        
laptop1 = Laptop("Asus", 32, 1000)
laptop1.upgrade_ram()
laptop1.display_info()

