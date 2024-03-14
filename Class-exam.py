# object is any entity that has attributes and behaviors. For example, a parrot is an object. It has

# attributes - name, age, color, etc.
# behavior - dancing, singing, etc.
# Similarly, a class is a blueprint for that object.

class students:
    # class attribute
    name = ""
    role_No = 0

# create Student1, Student2 object


student1 = students()
student1.name = "Varun"
student1.role_No = 67

student2 = students()
student2.name = "Savita"
student2.role_No = 68

print("Detail of student1   Name :", student1.name + " --- Role no :", student1.role_No)
print("Detail of student2   Name :", student2.name + " --- Role no :", student2.role_No)








