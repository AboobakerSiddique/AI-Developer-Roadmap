import add
import sub
import mul
import div

print('Welcome to calculator')
print('-----------------------')

while True:
    
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
    except ValueError:
        print('enter a valid number !')   
        break
    
    print('''
          
          1.Add
          2.Sub 
          3.Mul
          4.Div
          5.Exit
     
         ''')
    choice = int(input('what calculation(1/2/3/4/5): '))
    if choice == 1:
        add.add(a,b)
    elif choice == 2:
        sub.sub(a,b)
    elif choice == 3:
        mul.mul(a,b)
    elif choice == 4:
        div.div(a,b)
    elif choice == 5 :
        print('Thank you !')
        break
         
    