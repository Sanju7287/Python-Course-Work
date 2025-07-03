#1.Operations Of String

# Concatenation
s1="Python"
s2="Programming"
s=s1+" "+s2
print("Concatenation (+):",s) # Concatenation (+): Python Programming

# Repetition
print("Repetition (*):","Sanjay"*3) #Repetition (*): SanjaySanjaySanjay

# Indexing
a="chandrasanjaykumar"
print(a[3]) #Output: n
print(a[-7]) #Output:a

# Slicing
print(a[0:3]) #Output: cha
print(a[-3:-2]) #Output: m

# Membership
text="sanjay"
print("In operator:","sanjay" in text) # In operator: True
print("Not In operator:","vikash" not in text) # Not In operator: True

#2.Built-in String Functions

# len()
a="Sanjay"
print(len(a)) # Output: 6

# max() and min()
print(max("SanjayKumar")) # Output: 'y' (highest ASCII value)
print(min("SanjayKumar")) # Output: 'K' (highest ASCII value)

# sorted()
print(sorted("Sanjaykumar")) # Output: ['S', 'a', 'a', 'a', 'j', 'k', 'm', 'n', 'r', 'u', 'y']

# chr() and ord()
print(ord('a')) # Output: 97 (ASCII value of 'a')
print(chr(84)) # Output: 'a' (character for ASCII value 84)

#3.Case Conversion Methods
print("sanjay".upper()) # Output: SANJAY (upper() Method)
print("SANJAY".lower()) # Output: sanjay (lower() Method)
print("sanjay".capitalize()) # Output: Sanjay (capitalize() Method)
print("sanjay kumar".title()) # Output: Sanjay Kumar (title() Method)
print("Sanjay".swapcase()) # Output: sANJAY (swapcase() Method)
print("Straße".casefold()) # Output: strasse (casefold() Method)

#4.Alignment & Formatting Methods
print("Sanjay Kumar".center(20, "*")) # Output: ****Sanjay Kumar****(center() method)
print("Sanjay".ljust(10, "-")) # Output: Sanjay----(ljust() method)
print("Sanjay".rjust(10, "_")) # Output: ____Sanjay(rjust() method)
print("14".zfill(6)) # Output: 000014(zfill() method)

#5.Search & Find Methods
print("hello".find("l")) # Output: 2 (find() method)
print("hello".rfind("l")) # Output: 3 (rfind() method)
print("hello".index("e")) # Output: 1 (index() method)
print("hello".rindex("l")) # Output: 3 (rindex() method)
print("friends".count("r")) # Output: 1 (count() method)