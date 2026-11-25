# calculator  
x = int(input("Enter the first number :"))
z = input("Enter the operator (e.g. +, -, *, /, //, %, **):")
y = int(input("Enter the second number :"))
if z =="+":
    print("The result of",x,z,y,"is",x+y)
elif z =="-":
    print("The result of",x,z,y,"is",x-y)
elif z =="*":
    print("The result of",x,z,y,"is",x*y)
elif (z =="/" or z =="//" or z == "%") and y ==0:
    print("Invalid input , 2nd number cannot be zero in this operator")
elif  z =="/":
    print("The result of",x,z,y,"is",x/y)
elif z =="//":
     print("The result of",x,z,y,"is",x//y)
elif z =="%":
    print("The result of",x,z,y,"is",x%y)
elif z =="**":
    print("The result of",x,z,y,"is",x**y)
else :
    print ("Invalid operator") 
