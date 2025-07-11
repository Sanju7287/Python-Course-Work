# Tuples
t=()
t=(1,3,7.9,"vikash",{1,2,3},[1,2,3],True,3+7j)
print(t)
print(t[2])
print(t[-1])
print(t[1:3])
#concatenation
t1=(1,6)
t3=(0,9,7)
t2=t1+t3
print(t2)
print(t2*2)
print(1 in t1)
print(5 not in t3)
  

 #tuple unpacking 
a=(1,3,4)
x,y,z=a
print(x,y,z)

a=(1,4,5,8,9,8)
(1,4,5,8,9,8).count(8)
print(a)