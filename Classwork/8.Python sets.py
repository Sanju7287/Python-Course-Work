# sets
t={1,3,4,5}
print(t)
print(type(t))

t1={1,2.3,"vikash",True,9+5j,}
print(t1)
print(type(t1))
t1.add(23)
print(t1)
print(23 in t1)
print(23 not in t1)

# union,intersection,difference,symmetric Difference
b={"vikash","ramana","anem","sanjay"}
l={"python","java","c++","c#"}
b.add("rahul")
print(b)
res=b | l
print(res)
res=b ^ l
print(res)
res=b & l
print(res)
res=b - l

#subset and superset,isdisjointset
s={1,2,3}
s1={1,2,3,4}
print(s<=s1)
print(s>=s1)
print(s.isdisjoint(s1))
s.add(6)
print(s)
s.remove(1)
print(s)
s.discard(2)
print(s)
s1.pop()
print(s)
s1.clear()
print(s)
res=s.update(s1)
print(res)

s2={1,6,4,5}
s3={1,2,5,2,6}
s2=s3.copy()
print(s2)
print(len(s2))
print(max(s2))
print(min(s2))
print(sum(s2))
print(sorted(s3))
res=set([1,2,3])
print(res)