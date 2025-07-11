#dictionary
stud={'name':'vikash','rollno':66,'passedout':2025}
print(stud)
#accessing values
print(stud['name'])
print(stud.get("rollno"))
print(stud.get("university"))
#adding and update
stud["collage"]='mgit'
print(stud)

del stud['collage']
print(stud)
stud.popitem()
print(stud)
stud.clear()
print(stud)

#Dictonary Built-in Methods
# dict.clear()
dict={"name":'ramana','id':90}
dict.clear()
print(dict)

#dict.copy()
dict={"name":'ramana','id':90}
copy=dict.copy()
print(copy)

#dict.get(key,dafault=None)
dict={'a':1}
print(dict.get('a'))
print(dict.get('b',0))

#dict.items
dict={'a':1,'b':2}
print(list(dict.items()))

#dict.keys()
dict={'a':1,'b':2}
print(list(dict.keys()))


#dict.pop(key, default)
dict = {'a': 1, 'b': 2}
value = dict.pop('a')
print(value)    
print(dict)

#dict.popitem()
dict = {'a': 1, 'b': 2}
item = dict.popitem()
print(item)  
print(dict)   

#dict.update(other_dict)
a = {'x': 1}
b = {'y': 2}
a.update(b)
print(a)