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

#6.String Testing Methods (Boolean Results)
print("vikash".startswith("vik")) #Output: True (startswith() method)
print("Hemanth".endswith("th")) #Output: True (endswith() method)
print("Friends12".isalpha()) #Output: False (isalpha() method)
print("Vikash123".isalnum()) #Output: True (isalnum() method)
print("sanjay".islower()) #Output: True (islowe() method)
print("HEMANTH".isupper()) #Output: True (isupper() method)
print("Hello Friends".istitle()) #Output: True (istitle() method)
print("Vikash123".isidentifier()) #Output: True (isidentifier() method)
print("Vikash123".isdecimal()) #Output: False (isdecimal() method)
print("716264706".isdigit()) #Output: True (isdigit() method)
print("Madhav".isnumeric()) #Output: False (isnumeric() method)

#7.Replace & Modify Methods
print("madhav".replace("m","d")) #Output: dadhav (replace() method)
print("sheshu".translate(str.maketrans("h","u"))) #Output: suesuu (translate() method)
print("gopi".maketrans("op","@%")) #Output: {111: 64, 112: 37} (maketrans() method)


#6. Splitting & Joining Methods
text1="sanjay"
print(text1.split(" "))#Splits the string into a list by sep
print(text1.rsplit(" "))# Splits from the right side.
print("text1".splitlines(" "))#Splits at line breaks ( ).
result=' '.join(text1)# Joins elements with a separator.
print(result)
text2="hello-world"#Splits into a 3-part tuple at first sep.
print(text2.partition("-"))
print(text2.rpartition("-"))# Splits into a3-part tuple at last sep.

#7. Whitespace & Trimming Methods
print("  hello ".strip()) #Removes leading and trailing characters (default: spaces).
print("----hello".lstrip("-"))#Removes leading characters.
print("hello----".rstrip("-")) #Removes trailing characters.

#10.Encoding & Decoding Methods
print("vikash".encode("utf-7")) #Output: b'vikash'
print(b'vikash'.decode("utf-7")) #Output: vikash