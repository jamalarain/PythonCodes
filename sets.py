# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:59:52 2019

@author: Chakra IT
"""

#set nd frozen set


a={}
print(type(a))

b=set()
print(type(b))


s1={1,2,3,4,1,5}
s1
type(s1)
s1.add(6)
s1



s2=frozenset({6,7,8,9,5,6})
s2
type(s2)
s2.add(1)
s2


#set operations

s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
 
4 not in s1

#add
s1.add(55)
s1

#insert does not work
s1.insert(66)
s1
s1.insert(66,77)
s1
####################################
s1.remove(6)
s1

s1.remove(5)
s1

s1.remove(5)
s1

s1.discard(4)
s1
# update

s1={1,2,3,4,5}
s1.update({6,7,8})
s1

# add list and set
s1={1,2,3,4}
s1.update([4,5],[1,6,8])
s1


#union
s1.union(s2)  #s2.union(s1)
s1 | s2
s3=s1.union(s2)
s3


#intersection
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}

s1 & s2
s1.intersection(s2)
s3=s1.intersection(s2)
s3


# difference
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}

s1.difference(s2)
s3=s1.difference(s2)
s3=s1-s2
s3


#clear
s1
s1.clear()
s1
      

s1<s2  

s4={1,2,3,1,2,4,5}
s4

s={"hello world","hello King"}
s
print(s.pop())

print(s4.pop())

