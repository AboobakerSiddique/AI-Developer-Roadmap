#Requirements
#Create a tuple containing 5 compulsory subjects.

#Example:
#Math
#Physics
#Chemistry
#English
#Computer Science

#Create a set containing the extracurricular clubs a student joins.
#Intentionally add duplicates, 

#for example:
#Coding
#Music
#Coding
#Football
#Music
#Print:
#All compulsory subjects (tuple).
#All clubs (set).
#Total number of clubs after duplicates are removed.


compulsory_subjects=("Math",'English','Computer Science','Chemistry','Physics')
extras={"coding","music","coding",'football','music','music','cricket'}
print(f"compulsory subjects for new joinees: {compulsory_subjects}")
print(f"extracurricular clubs a student can joins: {extras}" )
print(f"Total extracurricular clubs: {len(extras)}")
