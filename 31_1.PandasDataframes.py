#In Pandas Series is one dimentional data structures
#Data frames are two dimentional data structures.

import pandas as pd 
 
#grouping data in data frames 
import os
os.getcwd()
os.chdir('E:\Office\Python\Rk\PYTHON_OCT2018-master2\data')
os.getcwd()

import pandas as pd
#headers=['Name','Title','Department','Salary']
chicago=pd.read_csv('ChicagoEmployees.csv',header=None) # reading with header / with out header header=1
chicago.shape
chicago.info()
chicago.describe()
#chicago
########################Slicing#################################
print(chicago.head())
dept=chicago.groupby(2)
dept.count().head()
#dept.size()
dept.size().head()

##########################files#########################################
titanic=pd.read_excel('titanic.xls',header=None) # reading with header / with out header header=1
titanic.shape
titanic.info()
titanic.describe()

titanic['survived'].mean()
pd.value_counts(titanic['survived']).plot.bar()
titanic.groupby(['sex']).mean()
##########################merge#########################################
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                     'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                     'value': [5, 6, 7, 8]})

df1.merge(df2, left_on='lkey', right_on='rkey')

df1.merge(df2, left_on='lkey', right_on='rkey',
          suffixes=('_left', '_right'))


df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False))

###########################################################################

