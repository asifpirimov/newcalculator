import math
def sum(x, y):
    return x + y
def emission(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y
def promotion(x, y):
    return pow(x,y)
def sqrt(a):
    return math.sqrt(a)
def log(x,y):
    return math.log(x,y)    
def factorial(a):
    return math.factorial(a)   
print("Hello my calculator!")



print("Please Select prosess: \n",
    "1.Sum \n"
    "2.Emission \n"
    "3.Multiplication \n"
    "4.Division \n"
    "5.Promotion \n"
    "6.SQRT \n"
    "7.Logorithm \n"
    "8.Factorial \n"
)
select = int(input("Select prosess 1,2,3,4,5,6,7,8:"))
if select == 1:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",sum(x, y))
elif select == 2:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",emission(x, y))
elif select == 3:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",multiplication(x, y))
elif select == 4:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",division(x, y))
elif select == 5:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",promotion(x, y))
elif select == 6:
    a = int(input("Enter a: "))
    print("Your answer is: ",sqrt(a))
elif select == 7:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print("Your answer is: ",log(x, y))
elif select == 8:
    a = int(input("Enter a: "))
    print("Your answer is: ",math.factorial(a))
else:
    print("Select corrrect prosses, please.")   
print("Thank you!")






    
