# Defining a function

def addition(param1, param2):
  print(param1 + param2)

addition(50, 60)
addition("Suhrith", " Nishritha")

firstnumber = 4
secondnumber = 5
print (firstnumber * secondnumber + secondnumber * firstnumber)

# Built-in Functions

print ("Hi")
print(str(5.6))
print(int("5"))
print(float("5.6"))
print(bool("True"))
print(len("Hello"))
print(len(["Hi","Hello"]))
readysort = [16,8,23,6]
mysort = sorted(readysort)
print(mysort)
#print(sorted["B","A","d","f","2","1","3.4","1.2"])

# Defined FUnctions

def my_function():
  print("I am defining my first function!")
  print("Hello World")

my_function()

#Passing arguements to the function

def multiply(num1,num2):
  print(num1 * num2)

num1=12
num2=13
print("firstnumber= ", num1, "secondnumber= ", num2)
multiply(num1, num2)