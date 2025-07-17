#*
for row in range(5):
    for col in range(5):
        print("*",end=" ")
    print()
#row 
for row in range(5):
    for col in range(5):
        print(row,end=" ")
    print()
#col  
for row in range(5):
    for col in range(5):
        print(col,end=" ")
    print()
    
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print("*",end=" ")
    print()
    
#row+1
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()
    
n=int(input("Enter the size:"))
for row in range(n):
    for spa in range(n-row-1):
        print(' ',end=' ')
    print()