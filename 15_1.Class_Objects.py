# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''Here, the self is used as a reference variable which refers to the current class object.
It is always the first argument in the function definition. 
However, using self is optional in the function call.'''
class Employee:  
    id = 10;  
    name = "ayush"  
    def display (self):  
        print(self.id,self.name)  
        
#<object-name> = <class-name>(<arguments>)
#The following example creates the instance(object) of the class Employee.
class Employee:  
    id = 10;  
    name = "John"  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp = Employee()  
emp.display()  

#Creating the constructor in python
'''the method __init__ simulates the constructor of the class. 
This method is called when the class is instantiated. 
We can pass any number of arguments at the time of creating the class object, 
depending upon __init__ definition. It is mostly used to initialize the class attributes. 
Every class must have a constructor, even if it simply relies on the default constructor.'''

#example to initialize the Employee class attributes.
class Employee:  
    def __init__(self,name,id):  
        self.id = id;  
        self.name = name;  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp1 = Employee("John",101)  
emp2 = Employee("David",102)  

emp1.display();   
emp2.display();   


#Example: Counting the number of objects of a class
class Student:  
    count = 0  
    def __init__(self):  
        Student.count = Student.count + 1  
s1=Student()  
s2=Student()  
s3=Student()  
print("The number of students:",Student.count)  


class Student:    
    # Constructor - non parameterized    
    def __init__(self):    
        print("This is non parametrized constructor")    
    def show(self,name):    
        print("Hello",name)    
student = Student()    
student.show("John")    


class Student:    
    # Constructor - parameterized    
    def __init__(self, name):    
        print("This is parametrized constructor")    
        self.name = name    
    def show(self):    
        print("Hello",self.name)    
student = Student("John")    
student.show()  


class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
  
#creates the object of the class Student  
s = Student("John",101,22)  
  
#prints the attribute name of the object s  
print(getattr(s,'name'))  
  
# reset the value of attribute age to 23  
setattr(s,"age",23)  
  
# prints the modified value of age  
print(getattr(s,'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s,'id'))  
# deletes the attribute age  
delattr(s,'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)  


class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
s = Student("John",101,22)  
print(s.__doc__)  
print(s.__dict__)  
print(s.__module__)  


class person:  
    def __init__(self):  
         self.name = "abc"; 
         self.gender = "male"; 
         self.age = 23; 
    def talk (self):  
        print("Hi i am ", self.name)  
    def vote (self):  
         if self.age>18 :
             print("I am not elgible to vote ")  
         else :
             print("I am elgible to vote ")  
        
obj=person()
person.talk(obj)
person.vote(obj)

obj.talk()


class person:  
    def __init__(self,n,g,a):  
         self.name = n; 
         self.gender = g; 
         self.age = a; 
    def talk (self):  
        print("Hi i am ", self.name)  
    def vote (self):  
         if self.age>18 :
             print("I am not elgible to vote ")  
         else :
             print("I am elgible to vote ")  
        
obj1=person("abc","Male",23)
obj2=person("abcd","Males",24)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()

