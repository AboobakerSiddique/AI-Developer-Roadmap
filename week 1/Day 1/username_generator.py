<<<<<<< HEAD
#Ask for:
#First name
#Last name
#Favorite number
#Generate 3 usernames.
#Example

#U#sername 1
#aboobaker_siddique

#Username 2
#abo123

#Username 3
#as123

print("---------Username Generator--------")
first_name=input("your first name: ")
last_name=input("your last name: ")
year_of_birth=input("year you are born: ")

username_1=(f"username1: {first_name.lower()}_{last_name.lower()}")
username_2=(f"username2: {first_name[0:3].lower()}{year_of_birth}")
username_3=(f"username3: {first_name[0].lower()}{last_name[0].lower()}{year_of_birth}")

print(username_1)
print(username_2)
=======
#Ask for:
#First name
#Last name
#Favorite number
#Generate 3 usernames.
#Example

#U#sername 1
#aboobaker_siddique

#Username 2
#abo123

#Username 3
#as123

print("---------Username Generator--------")
first_name=input("your first name: ")
last_name=input("your last name: ")
year_of_birth=input("year you are born: ")

username_1=(f"username1: {first_name.lower()}_{last_name.lower()}")
username_2=(f"username2: {first_name[0:3].lower()}{year_of_birth}")
username_3=(f"username3: {first_name[0].lower()}{last_name[0].lower()}{year_of_birth}")

print(username_1)
print(username_2)
>>>>>>> 19cf409537d03ea7dd0b41aebe7c5c7c14da08cd
print(username_3)