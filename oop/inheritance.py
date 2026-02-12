class Animal:
  def speak(self):
    print("Animal makes sound")
class Dog(Animal):
    def bark(self):
      print("Dog barks")

d= Dog()
d.speak()
d.bark()

#types of inheritance
#1.single inheritance
class Parent:
    def parent_method(self):
        print("This is the parent method.")
class Child(Parent):
    def child_method(self):
        print("This is the child method.")

c=Child()
c.parent_method()
c.child_method()


#2.multiple inheritance
class Father:
    def father_method(self):
        print("This is the father method.")
class Mother:
    def mother_method(self):
        print("This is the mother method.")
class Child(Father,Mother):
    def child_method(self):
        print("This is the child method.")
c=Child()
c.father_method()
c.mother_method()
c.child_method()  


#3.multilevel inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")
class Child(Parent):
    def child_method(self):
        print("This is the child method.")
c=Child()
c.grandparent_method()
c.parent_method()
c.child_method()


#4.hierarchical inheritance
class Parent:
    def parent_method(self):
        print("This is the parent method.")
class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")
class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")

c1=Child1()
c2=Child2()
c1.parent_method()
c1.child1_method()
c2.parent_method()
c2.child2_method()

#hybrid inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")
class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")
class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")

c1=Child1()
c2=Child2()
c1.grandparent_method()
c1.parent_method()
c1.child1_method()
c2.grandparent_method()
c2.parent_method()
c2.child2_method()
