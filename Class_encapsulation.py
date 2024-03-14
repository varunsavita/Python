# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"


class employee:
    # constructor
    def __init__(self, name, salary, project, BU):

        # public data member : Accessible anywhere from outside of a class.
        # Public data members are accessible within and outside of a class.
        # All member variables of the class are by default public.
        self.name = name
        self.BU = "Industrial"

        # private member : Accessible within the class
        self.__salary = salary

        # Protected member : Accessible within the class and its sub-classes
        self._project = "Tech"

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'BU:', self.BU)

    # public instance methods
    def inform(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

class employeeDetail (Company):
    # Accessing protected member in child class
    def showProject(self):
        print("Working on project :", self._project)

# creating object of a class
emp = employee('Varun', 80000, 'Technical', 'Fire')

# accessing public data members
print("Name: ", emp.name, 'BU:', emp.BU)

# calling public method of the class
emp.show()

# accessing private data members
#print('Salary:', emp.__salary) # uncomment it and test

# We can access private members from outside of a class using the following two approaches

# Create public method to access private members
emp.inform()

# Use name mangling

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._employee__salary)

emp2 = employeeDetail()
emp2.showProject()


# Direct access protected data member
print('Project:', emp._project)