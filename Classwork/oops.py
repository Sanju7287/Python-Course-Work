'''try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number: "))
    print(b)
    c=1+12
except NameError:
    print("a is not defined")
except IndexError:
    print("you have entered out of range")
except KeyError:
    print("Key is not defined")
except TypeError:
    print("you can't give 2 diff values")

except ValueError:
    print("Enter the proper data type") #or instead of use this one except (NameError,IndexError,KeyError,TypeError,ValueError) as e: print(f"Error occured:{e}")
else:
    print("No errors")
    print(c)
finally:
    print("code executed")'''
try:
    amount=int(input("Enter the amount: "))
    if amount<0:
        raise ValueError("Enter the positive value")
except Exception as e:
    print(f"Error occured:{e}")
else:
    print("No errors")
    print("You can withdraw")
finally:
    print("-----------Remove your card-----------")