import os

# get the current Directory
print(os.getcwd())

# change directory
os.chdir('D:\\Python')

print(os.getcwd())
os.chdir('D:\\Python\pythonLearning')
'''
os.mkdir('test567777')

print(os.listdir())

# rename a directory
os.rename('test567777','test123444')
print(os.listdir())
'''
# delete "myfile.txt" file
os.remove("myfile.tx")
print(os.listdir())