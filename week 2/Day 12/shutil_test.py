import os
import shutil

import os


print(os.getcwd())#to print current directory
shutil.copy('sample.txt','sample_copy.txt')#to copy a file
os.mkdir('test')#to create a folder
shutil.move('sample_copy.txt','test')#to move a file
os.rename('sample.txt','sample_1.py')#to rename

#shutil.rmtree('test')
