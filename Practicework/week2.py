#Automated salary tax
salary=int(input())
if 0<salary<=250000:
    print("No Tax")
elif 250001<salary<=500000:
    print(salary*0.05)
elif 500001<salary<=1000000:
    print(salary*0.2)
elif salary<100000:
    print(salary*0.3)
    
#Movie ticket pricing system
n=int(input())
total_price=0
for i in range(n):
    age=int(input())
    if age<5:
        continue
    elif 5<=age<=18:
        total_price+=100
    elif 19<=age<=60:
        total_price+=150
    elif age>60:
        total_price+=120
print(total_price)

#Electricity bill generator
units=int(input())
if units<=100:
    print(units*1.5)
elif 101<=units<=200:
    bill=100*1.5+(units-100)*2.5
    print(bill)
elif 201<=units<=500:
    bill=(100*1.5)+(100*2.5)+(units-200)*4
    print(bill)
elif units>500:
    bill=(100*1.5)+(100*2.5)+(300*4)+(units-500)*6
    print(bill)

#Car parking fee calculator
hr=int(input())
if hr<=2:
    print(30)
elif 2<hr<24:
    print(30+(hr-2)*10)
elif hr==24:
    print(200)

#Product Inventory Checker(Nested condition)
product=input()
qua=int(input())
if qua==0:
    print(f'{product}:Out of Stock')
elif 1<=qua<=10:
    print(f'{product}:Low Stock')
elif 11<=qua<=50:
    print(f'{product}:In Stock')
elif qua>50:
    print(f'{product}:Overstocked')
    
#Pattern row wise alternating 0 and 1(nested loops)
n=int(input())
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()
    
#Gym subscription billing(menu driven program)
