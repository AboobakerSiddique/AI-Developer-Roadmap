class Fan:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.speed = 0
        self.max_speed = int(max_speed)
        self.turned_on = False
        
    def turn_on(self):
        if self.turned_on:
            print("Fan is already on")
        else:
            self.turned_on = True
            self.speed = 1
            print(f"Fan is turned on\nnow speed is {self.speed}")
            
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            self.speed = 0
            print("fan is turned off")
        else:
            print("fan is already off")
    
    def increase_speed(self):
        if not self.turned_on:
            print("First turn on the fan")
        elif self.speed < self.max_speed:
            self.speed += 1
            print(f"Fan speed increased\nnow speed is {self.speed}")
        else:
            print("Max speed achieved")
            
    def decrease_speed(self):
        if not self.turned_on:
            print("First turn on the fan")
        elif self.speed > 1:
            self.speed -= 1
            print(f"Fan speed decreased\nnow speed is {self.speed}")
        else:
            print("Min speed achieved")
            
    def __str__(self):
        state = "ON" if self.turned_on else "OFF"
        return f"{self.brand} fan is {state} (Speed: {self.speed})"
        
fan1 = Fan('Usha',6)
print(fan1)        # Usha fan is OFF (Speed: 0)
fan1.turn_on()     # Fan is turned on, now speed is 1
fan1.increase_speed() # Fan speed increased, now speed is 2
print(fan1)      
fan1.increase_speed()
fan1.increase_speed()
fan1.increase_speed()  
print(fan1)   
fan1.increase_speed()
print(fan1)   
        
        