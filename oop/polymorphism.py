#polymorphism is the ability of an object to take on many forms. In python,
# polymorphism allows us to define methods in the child class with the same name as defined in their parent class. 
# It is used to perform a single action in different ways.

#1. method overloading - same method name with different parameters
class student:
    def info(self,name):
        print("Name:",name)
    def info(self,name,age):
        print("Name:",name,"Age:",age)

s = student()
# s.info("John")  # This will raise an error because the method info is defined twice with different parameters,
#  and the second definition will overwrite the first one
s.info("John", 20)  # This will work because the second definition of info is the one that is used here


#2. method overriding - same method name in parent and child class

class parent:
    def info(self):
        print("This is parent class")
class child(parent):
    def info(self):
        print("This is child class")

p = parent()
p.info()  # This will call the info method of the parent class 
c = child()
c.info()  # This will call the info method of the child class, which overrides the info method of the parent class 



#3. operator overloading - same operator with different meanings

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return point(self.x + other.x, self.y + other.y)

p1 = point(1, 2)
p2 = point(3, 4)
p3 = p1 + p2  # This will call the __add__ method of the point class, which adds the x and y coordinates of the two points
print("p1:", p1.x, p1.y)  # Output: p1: 1 2
print("p2:", p2.x, p2.y)  # Output: p2: 3 4
print("p3:", p3.x, p3.y)  # Output: p3: 4 6
