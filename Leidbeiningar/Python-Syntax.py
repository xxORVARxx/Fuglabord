#!/usr/bin/env python3


###
###  To Run Script Do:
###  python3 ./Python-Syntax.py 
###


### Import Module:
import math







print("Hello World")
print("~" * 10)

student_count = 1000
rating = 4,99
is_published = False
course_name = """
Multiple
Lines
"""

x, y = 1, 2

z = w = 1


print(type(student_count))


# 'Static' vs 'Dynamic' language:
age = 20
age = "Tutugu"


# 'Mutable' vs 'Immutable' types:
x1 = 1
print("Adress of x1:", id(x1))
x1 = x1 + 1
print("Adress of x1:", id(x1))

z1 = [1, 2, 3]
print("Adress of z1:", id(z1))
z1.append(4)
print("Adress of z1:", id(z1))



course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:6])
print(course[7:-1])


# Double quotes in string:    \"   \'   \\   \n
message = "'Best' Programming"
print(message)
message = '"Best" Programming'
print(message)
message = "\"Best\" Programming"
print(message)
message = "Best \nProgramming"
print(message)


# Formatted strings:
first = "    örvar"
last = "sigþórsson"
full = first + " " + last
#better_full = f"{first} {last}"

print(full.upper())
print(full.lower())
print(full.title())
print(full.strip())

print(full.find("var"))
print(full.find("vAr"))
print(full.replace("r", "R"))

print("þór" in full)
print("Þór" in full)
print("hommi" not in full)


# Binary numbers:
i = 5
print("Binary:")
print(bin(i))

i = 0b001
print(i)
i = 0b010
print(i)
i = 0b011
print(i)
i = 0b100
print(i)
i = 0b101
print(i)

# Hexadecimal numbers:
i = 0xff
print("Hex:")
print(i)
print(hex(i))


# Complex numbers:  ( python notar 'j' í staðin fyrir 'i' )
# a + bi
x = 1 + 2j
print("Complex numbers:")
print(x)


print("Operators:")
# Operators:
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3 # <- Floating point numbers.
print(x)
x = 10 // 3 # <- Integers.
print(x)
x = 10 % 3 # <- Modulus operator.
print(x)
x = 10 ** 3 # <- Exponent, 10 to the power of 3.
print(x)

x += 1
x -= 3
x *= 3
x /= 3
x //= 3
x %= 3
x **= 3
# In Python we Dont have 'x++' or 'x--'



# In Python we dont have 'constant variable',
# So use uppercase variable name emulate const variable.
PI = -3.14


# You Can Google 'Python 3 built-in functions' for list of functions.
# 'https://docs.python.org/3/library/functions.html'
print("https://docs.python.org/3/library/functions.html")

print(round(PI))
print(abs(PI))


# You Can Google 'Python 3 math module' for list of functions.
# https://docs.python.org/3/library/math.html
print("https://docs.python.org/3/library/math.html")

# Using the 'math' module:
print(math.floor(PI))


# Get 'Input' from user:
my_input = input("Input a Number: ")


### Type conversion:
# Python is a 'strongly-typed' language,
# doesn't do any type conversion automatic.


# y = my_input + 1     <-- ERROR, Can't convert 'int' to 'string'.

# Built in type conversion functions:
print(str(my_input))
print(bool(my_input)) # Falsy-values: '""', '0', '[]' or 'None'(null in c++).
print(float(my_input))
print(int(my_input))


# Conditional Statements:
age = 22
if age >= 18:
    print("Adult.")
elif age >= 13:
    print("Teenager.")
else:
    print("Child")

if age == 18:
    pass #  <-- Use the 'pass' keyword for empty staments.
if age != 18:
    pass


# Logical Operators:  'and'  'or'  'not'
name = "Mosh"
# Checking if name is an empty string:
if not name:
    print("1. Name is empty.")
    
name = ""
if not name:
    print("2. Name is empty.")

name = " "
if not name:
    print("3. Name is empty.")

if not name.strip(): #  <-- Remove Whitespace.
    print("4. Name is empty.")

age = 22
if age >= 18 and age < 65:
    print("Eligible.")

# Chaining Comparison Operators:
if 18 <= age < 65:
    print("Also Eligible.")


    
# The Normal Way:
if age >= 18:
    message = "Is Eligible."
else:
    message = "Not Eligible."
print(message)

# The Other Way:   (Ternary Operators)
#message = age >= 18 ? "Is Eligible." : "Not Eligible."
#print(message)

# The Python Way:
message = "Is Eligible." if age >= 18 else "Not Eligible."
print(message)



### Python have 2 types of loops:  'for'  'while'
# The 'for' loop can iterate through iterable-objects:

for i in "Python.":  # <-- Loop through string.
    print(i)

for i in ['A', 'B', 'C', 'D', '.']: # <-- Loop through list.
    print(i)

for i in range(5): # <-- Loop through numbers.
    print(i)
print("")

for i in range(8, 12):
    print(i)
print("")

for i in range(0, 64+8, 8):
    print(i) 
print("")


# The 'range()' function dose not return a 'list':
print([0, 1, 2, 3, 4])  #  <-- This is a 'list' object.
print(range(5))  #         <-- This is a 'range' object.
print(type(range(5)))  #   <-- This is the type 'range' class.

# The difference between 'list' and 'range' objects is
# that a 'range' from 0 to billion takes no memory, but
# a 'list' from 0 to billion takes alot of memory.



print("Searching List:")

names = ["Eva", "Ívar", "Ásta"]
for name in names:
    if name.startswith("Á"):
        print("Found!")
        break  #  <-- Keyword, stop the loop.
else:
    # This will execute only if the loop dosent 'break'.
    print("Not found!")



### The 'while' loop:
guess = 0
answer = 5
while answer != guess:
    guess = int(input("Guess a number between 4 and 6: "))
else:
    pass



### Functions:
def My_function(x, y):
    pass  #  <-- Returns 'None'.


def Increment(number, by=1): # <-- Default argument.
    return number + by


def Const_increment(number, by):
    return(number, number + by)  #  <-- Returning two variable.



print("Function Returns:")
print(My_function(2, 3))
print(Increment(2, 3))
print(Increment(2)) # <-- Use the default argument.
print(Const_increment(2, 3))
print(type(Const_increment(2, 3))) 
# Class 'tuple'is like  read-only list.

# To make 'list' use: [x,y,z,w], to make 'tuple' use: (x,y,z,w).
t = ('x', 'y', 'z', 'w')
print(t)

# To make function-calls more readable you can use
# 'Keyword-arguments':
Increment(2, by=3)

# Python is a 'strongly-typed' language, you can use:
# Type hinting:
def Increment_numbers(number:int, by:int=1) -> int:
    return number + by


### Function with Arbitrary number of arguments:
# Just a normal function:
def Multiply(a, b): 
    return a * b


# You can do this with a list:
def Multiply_list(my_list):
    total = 1
    for i in my_list:
        total *= i
    return total


# You can do this with the '*'prefix to automatically
# converts the arguments to a 'tuple':
def Multiply_args(*my_arguments):
    total = 1
    for i in my_arguments:
        total *= i
    return total


print(Multiply(2, 2))  #  <-- Normal.
print(Multiply_list([2, 2, 2]))  #  <-- List.
print(Multiply_args(2, 2, 2, 2))  #  <-- '*'prefix (tuple).


# To go even further, you have the '**'prefix:
def Save_user(**user):
    print(user)
    print(type(user))  #  <--  'Dictionary'.
    print(user["name"])  # <-- Excess data in the 'dictionary'.
    

    
# Function call:
Save_user(id=1, name="Örvar", permit="admin") # <-- '**'prefix (Dictionary).



### Scope Resolution in Python ###
# In Python you only have two levels of scope: Global and Function.
# We dont have block level scope, like 'if'statements and 'loops'
# don't have their own scope.

var = 'a'  #  <-- Global variable. Not accessible in functions.
def Greet():
    if True:
        var = "b"  #  <-- Declaring a variable inside the 'if'statement.
    print(var)  #  <-- It is still accessible outside the 'if'statement.


Greet()
print(var) # The global variable is still 'a' not outside the function.



## The FizzBuzz Problem ##
# If the number is divisible by 3, print: 'Fizz'.
# If the number is divisible by 4, print: 'Buzz'.
# If the number is divisible by both 3 and 4, print: 'FizzBuzz'.

def Fizz_buzz(input):
    if input == 0:
        return
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return



for i in range(0, 32):
    if Fizz_buzz(i):
        print("For the number:", i, "=", Fizz_buzz(i))

