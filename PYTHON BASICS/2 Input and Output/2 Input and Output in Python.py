# Input and Output in Python
na = input("Enter your name: ")
print(na)

# Printing Variables
name1 = "Sumit"
age = 20
print("My name is", name1, "and my age is", age)

# Take Multiple Input in Python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is", name, "and my age is", age)

# Take Conditional Input from user in Python
age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
# How to Change the Type of Input in Python
age = input("Enter your age: ")
print(type(age))  # This will print <class 'str'>
age = int(age)  # Convert string to integer
print("Your age is", age)
print(type(age))  # This will print <class 'int'>

# Find the Datatype in Python
a = "Hello World"
b = 10
c = 10.5
d = True
e = [1, 2, 3, 4, 5]
f = {'key': 'value'}
g = (1, 2, 3)

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'list'>
print(type(f))  # <class 'dict'>
print(type(g))  # <class 'tuple'>