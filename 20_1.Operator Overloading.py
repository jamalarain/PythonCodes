# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:42:12 2019

@author: Chakra IT
"""
###################Magic Methods(which work behind the scene)###############
a=3
b=5
print(a+b)

int.
print(int.__add__(a,b))  #behnd the scene its calling

a='3'
b='5'
print(a+b)    # 3 and 5 are concatenated here#######################3

print(str.__add__(a,b))


__mul__
__sub__
########################Overloading   Will show error#################################
#we do not have the add method so it show error
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
        
s1=student(23,45)
s2=student(15,47)

s3=s1+s2 # we cannot use + sign between s1 and s2

##############################################
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
          
    def __add__(self,other):         #method oveloaad 
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        
        return s3
    
s1=student(23,45)
s2=student(15,47)
    
s3=s1+s2       # student(s1,s2)

print(s3.m1,s3.m2)
print(s3.m2)
######################################################
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
          
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        
        return s3
    
    def __gt__(self,other):      #ge can be used
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1 > r2:
            return True
        else:
            return False    
        

s1=student(23,45)
s2=student(15,47)
    
s3=s1+s2

print(s3.m1)

if s1 > s2:
     print("s1 wins")
else:
     print("s2 wins")    

##############################we get the error for _str_#############################
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
          
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        
        return s3
    
    def __gt__(self,other):     #adding and comparing
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1 > r2:
            return True
        else:
            return False    
     
    def __str__(self):
        return.self.m1, self.m2

s1=student(23,45)
s2=student(15,47)
    
s3=s1+s2

print(s3.m1)

if s1 > s2:
     print("s1 wins")
else:
     print("s2 wins")    
     

a=9
print(a)  #__Str__ happening behind the scene
print(a.__str__)


print(s1)   #we do not want address we want values

################################################################
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
          
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        
        return s3
    
    def __gt__(self,other):     #adding and comparing
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1 > r2:
            return True
        else:
            return False    
     
    def __str__(self):
        return '{} {} ' .format(self.m1, self.m2)

s1=student(23,45)
s2=student(15,47)
    
s3=s1+s2

print(s3.m1)

if s1 > s2:
     print("s1 wins")
else:
     print("s2 wins")    
     

a=9
print(a)  #__Str__ happening behind the scene
print(a.__str__)


print(s1)   #we do not want address we want values      

####################################################################
        
    
        
        
        
        