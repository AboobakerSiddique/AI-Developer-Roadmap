#Requirements
#Store:
#Name
#Age
#Course
#College
#CGPA
#Then:
#Print the entire dictionary.
#Print only the student's name.
#Update the CGPA.
##Add a phone number.
#Print the updated dictionary.

student_profile = {
    "Name": input("Enter student's name: "),
    "Age": int(input("Enter student's age: ")),
    "Course": input("Enter student's course: "),
    "College": input("Enter student's college: "),
    "CGPA": float(input("Enter student's CGPA: "))
}

print("----------------Student Profile--------------")
for key, value in student_profile.items():
    print(f"{key}: {value}")
print("---------------------------------------------") 
print("\n")  
print(f"student name : {student_profile['Name']}")
print("\n")
student_profile["CGPA"] = 9.0
student_profile["Phone Number"] = "123-456-7890"
print("----------------Student Profile--------------")
for key, value in student_profile.items():
    print(f"{key}: {value}")
print("---------------------------------------------") 