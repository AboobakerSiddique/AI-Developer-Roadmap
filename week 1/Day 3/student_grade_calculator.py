#Problem Statement

#Create a program that:
#Takes a student's:
#Name
#Marks
#Calculates the grade.
#Stores everything in a dictionary.
#Displays the result neatly.

#Grade Criteria
#90–100 → A+
#80–89 → A
#70–79 → B
#60–69 → C
#50–59 → D
#Below 50 → F

print("-----------Student Grade Report-----------")
name=input("Enter student's name: ")
marks=int(input("Enter marks for subject : "))
print("\n")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Failed!"
    
grade=calculate_grade(marks)

student_profile = {
    "Name": name.capitalize(),
    "Marks": marks,
    "Grade": grade
}

print("----------------Student Profile--------------")
for key, value in student_profile.items():
    print(f"{key}: {value}")
    
print("-----------------------------------------")