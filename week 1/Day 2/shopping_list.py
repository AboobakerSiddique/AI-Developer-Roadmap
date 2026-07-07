#Create a file named:
#shopping_list.py
#Requirements:
#Create an empty shopping list.
#Ask the user to enter 5 grocery items.
#Add each item to the list.
#Print:
#The complete shopping list.
#The first item.
#The last item.
#The total number of items.

print("--------Shopping List--------")
print("Add 5 items to shopping cart")
print("items available: ")

grocery_list=["Apples","Bun","Eggs","Chicken","Protein Powder","Soya","Kubz","Oats","Mango","Milk"]
print(grocery_list)

item_one=input("First item: ")
item_two=input("Second item: ")
item_three=input("Third item: ")
item_four=input("Fourth item: ")
item_five=input("Fifth item: ")

Customer_grocery_list=[item_one.capitalize(),item_two.capitalize(),item_three.capitalize(),item_four.capitalize(),item_five.capitalize()]
print("Your Shopping cart: ")
print(Customer_grocery_list)
print("First item: ")
print(Customer_grocery_list[0])
print("Last item: ")
print(Customer_grocery_list[4])
print("No.of.items: ")
print(len(Customer_grocery_list))