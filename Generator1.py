'''
A Python generator is a function which returns a generator iterator 
(just an object we can iterate over) by calling yield . yield may be called with a value, 
in which case that value is treated as the "generated" value.'''
'''#########################Generator##############################''' 
def G1(): 
   
    yield 3
  
values=G1()
print(values) 
#########################################################
def G1(): 
   
    return 3
  
samp=G1()
print(samp) 
#########################################################
def G1(): 
   
    yield 3
  
samp=G1()
print(samp.__next__()) 

#####################################################
def G1(): 
   
    yield 2
    yield 3
    yield 4
    yield 5
  
samp=G1()
print(samp.__next__()) 
print(samp.__next__()) 

for i in samp: 
    print(i)
############################################################

def G1(): 
   
    n=1
    
    while n< 10:
        sq=n*n
        yield sq
        n+=1
samp=G1()
print(samp.__next__()) 
print(samp.__next__()) 

for i in samp: 
    print(i)
############################################################









