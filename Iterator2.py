'''
Iterator in Python is simply an object that can be iterated upon. 
An object which will return data, one element at a time. Technically speaking, 
Python iterator object must implement two special methods, __iter__() and __next__() , 
collectively called the iterator protocol.

Each time we call the next method on the iterator gives us the next element. 
If there are no more elements, it raises a StopIteration .
'''
####################################################
l = [3,4,5,6] 
for i in l: 
    print(i)

it=iter(l)
print(it)
#################Not getting value####################
l = [3,4,5,6] 

it=iter(l)
print(it)
##########################################
l = [3,4,5,6] 

it=iter(l)
print(it.__next__())  #First it will give 3
print(it.__next__())  #Second it will give 4

print(next(it))  

for i in l: 
    print(i)
####################The loop willnot stop it prints the values#######################################
class Test: 
  
    def __init__(self): 
        self.num = 1 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        return self
  
    def __next__(self): 
        val=self.num
        self.num +=1
        
        return val
    
values=Test()

for i in values: 
    print(i)
############################To avoid above####################################
class Test: 
  
    def __init__(self): 
        self.num = 1 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        return self
  
    def __next__(self): 
        val=self.num
        self.num +=1
        
        return val
    
values=Test()
print(values.__next__())
print(values.__next__())
#############################################################
class Test: 
  
    def __init__(self): 
        self.num = 1 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        return self
  
    def __next__(self): 
        
        if self.num <=10:
            val=self.num
            self.num +=1
            
            return val
    
values=Test()
for i in values: 
    print(i)
##########################################################
class Test: 
  
    def __init__(self): 
        self.num = 1 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        return self
  
    def __next__(self): 
        
        if self.num <=10:
            val=self.num
            self.num +=1
            
            return val
        else:
            raise stopiteration
    
values=Test()
#print(next(values))  #if we have this it will not repeat it 
for i in values: 
    print(i)

############################################################
