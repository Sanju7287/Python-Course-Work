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
#space 
n=int(input("Enter the size:"))
for row in range(n):
    for spa in range(n-row-1):
        print(' ',end=' ')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(row):
        print(' ',end='')
    for col in range(n-row):
        print("*",end='')
    print()
    
for row in range(n):
    print(' '*row,end='')
    print("*"*(n-row),end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    if row<=n//2:
        print("*"*(row+1),end=' ')
    else:
        print("*"*(n-row),end=' ')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or (col==0 and row<n//2) or col==n-1 and row>=n//2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==0 or col==n-2:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if col==row or col==n-row:
            print("*",end='')
        else:
            print(" ",end='')
    print()    