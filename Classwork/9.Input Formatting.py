#input string formatting
name=input("enter the name: ")
print(name)

#input int formatting
num=int(input("enter the num: "))
print(num)

#input float formatting
decimal=float(input("enter the decimal: "))
print(decimal)

#input as list  formatting
names=input("enter students name: ").split()
print(names)

#list of integers
student_id=list(map(int,input("enter student id: ").split()))
print(student_id)

#list of floats
student_id=list(map(float,input("enter student id: ").split()))
print(student_id)

# list of str 
student_id=list(map(str,input("enter student id: ").split()))
print(student_id)

# tuple as input
student_id=tuple(map(int,input("enter student id: ").split()))
print(student_id)

#set as input
student_id=set(map(int,input("enter student id: ").split()))
print(student_id)

#dict input using
student_id=eval(input("enter user profile as a dictionary: "))
print(student_id)