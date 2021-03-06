import os
os.getcwd()
os.chdir("E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles")
os.getcwd()

# File modes(r,r+,w,w+,a,a+,etc..)
# Open a file from mentioned path
ft=open('date1209.txt','r')
ft=open('mdata.txt','r')
print(ft.read())

# Write a file
ft=open('mdata.txt','w')
ft.write('line-3')

#close a file 
ft.close()

ft=open('date1200.txt','w')
ft.write('line-2')
ft.write('line-3')
ft.close()

# read full file 
ft=open('date1209.txt','r')
ft.read()
ft.close()

# read file content only specific length data
ft=open('date1209.txt','r')
ft.read(5)
ft.close()

# read total line at a time
ft=open('date1209.txt','r+')
ft.readline()

ft=open('date1209.txt','r+')
ft.readlines()

# write multiple lines at a time
seq=['line-1\n','line-2\n']
ft=open('testfile2108.txt','r+')
ft.write('line-6')
ft.writelines(seq)
ft.write('\n')
ft.close()



# Other file functions
ft=open('date0808.txt','r+')
ft.tell()   # position of the control to read a file position
ft.read(5) 
ft.tell() 
ft.seek(0,1)   # to set the position
ft.tell()
ft.close()
ft=open('date0808.txt','w')
ft.write('line-5')
ft.close()

# to know whether file is closed or not.
ft.closed

#fp.seek(offset, from_what)
'''
where fp is the file pointer you're working with; offset means how many positions 
you will move; from_what defines your point of reference:

0: means your reference point is the beginning of the file
1: means your reference point is the current file position
2: means your reference point is the end of the file
if omitted, from_what defaults to 0.
'''
ft=open('date0808.txt','r')
ft.seek(0,0)   # to set the position
next(ft)
ft.close()

# other file functions to know about file
ft.closed
ft.name
ft.mode
ft.fileno()

'''
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: "), fo.name

fid = fo.fileno()
print ("File Descriptor: "), fid

# Close opend file
fo.close()
'''

ft=open('date0808.txt','w+')
ft.read(3)
ft.truncate(3)
ft.close()


ft=open('test.txt','a+')
ft.write("end")
ft.read()
ft.read(10)
ft.close()
ft=open('test.txt','r+')
ft.readline()
ft.readlines()
ft.close()
ft=open('test.txt','r+')
print(ft.readline())
ft.flush

#To delete a file you must import os module and run its os.remove() function
import os
os.remove('mdata.txt')

#check the file exists
import os
if  os.path.exists('mdata.txt'):
    os.remove('mdata.txt')
else:
    print('The file does not exist')

#deleting a folder
import os
os.rmdir('x')    

'''########To list all the files and path in the folder###########'''
import glob

path = 'E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)
##############FILES#############    
files = [f for f in glob.glob("**/*.txt", recursive=True)]

for f in files:
    print(f)

'''#################Read a CSV File#######################'''
import csv
with open('E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles\data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row) 
    
'''#################Read a CSV as a Dictionary#######################'''
    
reader = csv.DictReader(open("file2.csv"))
for raw in reader:
    print(raw)

'''#################write CSV File#######################'''    
with open('E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles\writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])


'''#################Reading CSV Files with Pandas#######################
Pandas is an opensource library that allows to you perform data manipulation in Python.
Pandas provide an easy way to create, manipulate and delete the data.

Reading the CSV into a pandas DataFrame is very quick and easy
'''        

import pandas
result = pandas.read_csv('E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles\data.csv')
print(result)


from pandas import DataFrame
C = {'Programming language': ['Python','Java', 'C++'],
        'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
        'Appeared': ['1991', '1995', '1985'],
        'Extension': ['.py', '.java', '.cpp'],
    }
df = DataFrame(C, columns= ['Programming language', 'Designed by', 'Appeared', 'Extension'])
export_csv = df.to_csv (r'E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles\pandaresult.csv', index = None, header=True) # here you have to write path, where result file will be stored
print (df)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    