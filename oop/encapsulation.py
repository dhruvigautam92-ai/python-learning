#encapsulation means wrapping data and methods together and restricting direct access to data
#using: Public, Private and Protected access modifiers

#1. public(default) - accessible from anywhere
class student:
     def __init__(self):
            self.name = "John"

s = student()
print(s.name) 



#2. protected - accessible within the class and its subclasses
class student:
     def __init__(self):
            self._name = "John" #protected variable
s = student()
print(s._name)  # This is accessible, but by convention, it should not be accessed directly outside the class or its subclasses



#3. private - accessible only within the class
class student:
     def __init__(self):
            self.__name = "John" #private variable
     def get_name(self):
         return self.__name

s = student()
print(s.get_name())
# print(s.__name)  # This would raise an error because __name is private
# To access private variables, we use a getter method


