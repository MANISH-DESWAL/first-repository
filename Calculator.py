#CALCULATOR

'''It's an simple calculator module that provides basic arithmetic operations 
having 2 variables as input and returning the result.'''

#creating functions for each operation
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b  

#main code
z="Yes"
while z.lower()=="yes":
        
        a=int(input("enter the first num:-- "))
        opr=input("enter the operator(+,-,*,/):-- ")
        b=int(input("enter the second num:-- "))

        if opr=="+":
            print(f"the addition of {a} and {b} is {add(a,b)}")

        elif opr=="-":
            print(f"the subtraction of {a} and {b} is {sub(a,b)}")

        elif opr=="/":
            print(f"the division of {a} and {b} is {div(a,b)}")

        elif opr=="*":
            print(f"the multiplication of {a} and {b} is {mul(a,b)}")

        else:
            print("invalid operator")

        z=input("Do you want to still use the calculator(yes/no):-- ")    

else:
    print("Thanks for using! exiting the calculator...")


