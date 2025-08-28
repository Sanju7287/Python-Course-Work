'''#read
try:
    file=open('demo.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    read=file.read()
    file.seek(0)
    readlines=file.readlines()
    file.seek(0)
    readline=file.readline()
    print(f"\nFile content using read():\n{read}")
    print(f"\nFile content using readlines():\n{readlines}")
    print(f"\nFile content using readline():\n{readline}")
    file.close()
finally:
    print("Rest of the code")
#write
try:
    file=open('dsda.txt','w')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam')
    file.close()
finally:
    print("Rest of the code")
#write+read
try:
    file=open('dsda.txt','w+')
except FileNotFoundError:
    print("File is not present")
else:
    file.write('Monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")
    
#r->read
#w->write
#a->append
#r+->read+write
#w+->write+read
#a+->append and read

#other way to write the code 
with open('dsda.txt','r+') as file:
    file.write('\nFile operations')
    file.seek(0)
    print(file.read())'''
    
import os
import shutil
print(os.getcwd())
if not os.path.exists('DSDA'):
    os.mkdir('DSDA') #creates a new directory
    #os.rmdir('DSDA') #remove the directory
    os.makedirs('DSDA\1234')
shutil.rmtree('DSDA')