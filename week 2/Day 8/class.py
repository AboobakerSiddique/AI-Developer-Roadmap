class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        self.turned_on = False
    
    def turn_on(self):
        if self.turned_on:
            print(f"{self.brand} is already turned on.")
        else:
            self.turned_on = True
            print(f"{self.brand} is now turned on.")
            
    def turn_off(self):
        if not self.turned_on:
            print(f"{self.brand} is already turned off.")
        else:
            self.turned_on = False
            print(f"{self.brand} is now turned off.")
            
    def run(self,seconds):
        if self.turned_on:
            print(f"{self.brand} is running for {seconds} seconds.")
        else:
            print(f"{self.brand} is turned off. Please turn it on first.")
            
    def __str__(self):
        print (f'{self.brand} (color: {self.color})')
    
    
volswagen = car("Volkswagen", "Blue")

maruti = car("Maruti", "Red")

volswagen.turn_on()
volswagen.run(5)
volswagen.turn_off()
volswagen.__str__()