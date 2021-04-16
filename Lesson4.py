
#Entering the values in the prompt

def addition(a, b):
    c = a + b
    print('The sum of {0} and {1} is {2}'.format(a, b, c))

def substraction(a, b):
    c= a - b
    print('The difference of {0} and {1} is {2}'.format(a, b, c))

def multiply(a, b):
    c= a * b
    print('The product of {0} and {1} is {2}'.format(a, b, c))

def division(a, b):
    c= a / b
    print('The division of {0} and {1} is {2}'.format(a, b, c))

a = input("Enter first number : ")
b = input("Enter second number : ")

print("Testing with integer values")
addition(int(a), int(b))
substraction(int(a), int(b))
multiply(int(a), int(b))
division(int(a), int(b))

print("Testing with float values")
addition(float(a), float(b))
substraction(float(a), float(b))
multiply(float(a), float(b))
division(float(a), float(b))
