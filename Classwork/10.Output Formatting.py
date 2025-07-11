# output formatting
a='vikash yadav'
print(a)
print(a[::-1])

name="vikash"
school="krrs"
Score=85
print("Name:" , name, "School:", school)
print('2025','07','09',sep="-")
print(name,end=" ")
print(school)
print("name \n school")
print("name \t school")
print("name: %s | school: %s | score: %d " % (name, school, Score))
print(f"name:{name} | score:{Score} | School:{school}")