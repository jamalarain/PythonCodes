class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname +'.'+ lname + '@email.com'
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)


emp1=emp('Rocky','Sandy')
print(emp1.fname)
print(emp1.email)
print(emp1.fullname())

########################################################3
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname +'.'+ lname + '@email.com'
    
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1=emp('Rocky','Sandy')

emp1.fname='Scott'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname())
'''#######################Using Property decortor##################################
Property decortor allows us to define a method or we can access like a attribute '''
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
                
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1=emp('Rocky','Sandy')

emp1.fname='Scott'

print(emp1.fname)
print(emp1.email())     #To continue this as an attribute see below
print(emp1.fullname())
###############################################################
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property           
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1=emp('Rocky','Sandy')

emp1.fname='Scott'

print(emp1.fname)
print(emp1.email)       #Changed
print(emp1.fullname())
###############################################################
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property           
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property 
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1=emp('Rocky','Sandy')

emp1.fname='Scott'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname)   #Changed
#####################Error when used fullname###################################
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property           
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property 
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp1=emp('Rocky','Sandy')

emp1.fullname='Rocky Sandy'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname)  
########################to overcome above######################################
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property           
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property 
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    @fullname.setter
    def fullname(self,name):
        fname, lname=name.split(' ')
        self.fname=fname
        self.lname=lname
        
        
emp1=emp('Rocky','Sandy')

emp1.fullname='Rockys Sandys'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname)  
############################Delete setter##################################### 
class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property           
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property 
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    @fullname.setter
    def fullname(self,name):
        fname, lname=name.split(' ')
        self.fname=fname
        self.lname=lname
        
    @fullname.deleter   
    def fullname(self):      #only self in deleter
        print('delete name!')
        self.fname=None
        self.lname=None
        
emp1=emp('Rocky','Sandy')

emp1.fullname='Rockys Sandys'

print(emp1.fname)
print(emp1.email)
print(emp1.fullname)  

del emp1.fullname
#################################################################




