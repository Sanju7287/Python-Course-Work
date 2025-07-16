
#Birthday
date,month,year=input().split('-')
print(f'{year}/{month}/{date}')

#Even &Odd
n=int(input())
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")

#Vowel Replacer
s=input().lower()
print(s.translate(str.maketrans('aeiou','*****')))

#Shopping cart Analyzer
l=list(map(float,input().split()))
print(sum(l))
print(max(l))
 
#Login credentials
credentials=("admin","python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("Login Successful")
else:
    print("Access Denied")

#Remove duplicates from set
names=set(input().split(','))
print(sorted(names))

#Student marks record(dict oper)
n=int(input())
data={}
max_val=0
res_name=''
for  _ in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        max_val=marks
        res_name=name
    data[name]=marks
print(data)
print(res_name)

#Reverse my words(string slicing)
sen=input().split()
for i in sen:
    print(i[::-1],end=' ')

#Clean my list
l=list(map(int,input().split()))
while(0 in l):
    l.remove(0)
print(l)

#clean my list 2
l=list(map(int,input().split()))
res=[]
for i in l:
    if i!=0:
        res.append(i)
print(res)

#The frequency counter(dict+str)
line=input()
data={}
for i in line:
    if i not in data and i!=' ':
        data [i]=line.count(i)
print(data)