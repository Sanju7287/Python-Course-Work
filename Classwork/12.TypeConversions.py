# converting from int
a=90
float(a)
print(a)
str(a)
print(a)
bool(a)
print(a)

# converting from float
a=9.9
int(a)
print(a)
str(a)
print(a)
bool(a)
print(a)

#converting from str
a="10"
int(a)
print(a)
a="10.0"
float(a)
print(a)
a="vikash"
list(a)
print(a)
tuple(a)
print(a)
set(a)
print(a)
bool(a)
print(a)

#converting from list
a=[1,3,4]
res=bool(a)
print(res)
a=[1,2,3]
res=str(a)
print(res)
res=set(a)
print(res)

list_d = (1, 2, 3, 4)
res=bool(list_d)
print(res)

# conertingfrom tuple
t=(1,3,4,6,7,8)
re=str(t)
print(re)
res=bool(t)
print(res)
res=list(t)
print(res)
res=set(t)
print(res)

# converting from set
a={3,5,8,6}
res=list(a)
print(res)
res=tuple(a)
print(res)
res=str(a)
print(res)
res=bool(a)
print(res)

#converting from dict
d={2:1,3:2,4:3}
res=str(d)
print(res)
res=bool(d)
print(res)
res=list(d)
print(res)
res=tuple(d)
print(res)
res=set(d)
print(res)

#converting bool
a=True
res=int(a)
print(a)
res=float(a)
print(a)
res=str(a)
print(a)