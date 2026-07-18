import os
print(os.getcwd())

def create():
    os.mkdir("images.txt")
    os.mkdir("images1.txt")
    os.mkdir("images2.txt")
    print('3 files created succesfully !!!')
    
def move():
    os.path.join('Day 12','images.txt')
    os.path.join('Day 12','images1.txt')
    os.path.join('Day 12','images2.txt')
    print('3 files moved succesfully !!!')
    
    
os.rmdir('images2.txt')

