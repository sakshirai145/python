'''
FUNCTION = To reduce the redundancy and introducing the reusability of code.
redundancy = The repetition of code that can be avoided.
reusability = The ability to use the same code many times.

OBJECT = to map with real-world entities or Scenarios , We start using Objects in code.
this is called Object-Oriented Programming (OOP).
example: list, tuple, set, dict, etc.

Classes: A class is a blueprint for creating objects. '''


#creating class
class Student:
    name = "Sakshi"

#creating object
s1 = Student()

print(s1.name)
 ##  Object also known as instance



'''CONSTRUCTOR =  A special method called when an object is created.'''



class School:
   name = "Sonam"
   def __init__(self):
      print("Constructor is called")

s1 = School()
print(s1) # Constructor is called  




class Schools:
   def __init__(self,fullname):
      self.name = fullname
      print("Adding student in school")

s2 = Schools("John")
print(s2.name)

s3 = Schools("Sakshi")
print(s3.name)




'''
ATRIBUTES = Variables that belong to an object.
  class attributes = Variables that are shared among all instances of a class.
  Instance attributes = Variables that are unique to each instance of a class.
'''

class employee:
   company_name = "Google" 
   name = "John Doe" # class attribute

   def __init__(self, emp_id):
       # obj attr > instance attribute(same name periority)
       self.emp_id = emp_id # instance attribute
       print("adding new employee")

E1 = employee(101)
print(E1.name) 




'''
METHODS = it is a function that belongs to an object.
'''
