file = open("notes.txt", "w")
file.write("Learning Python \nLearning Git \nLearning AI")
file.close()
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
with open("notes.txt", "a") as file:
    file.write("\nLearning File Handling")
    
print()
    
print("Updated content:")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)  