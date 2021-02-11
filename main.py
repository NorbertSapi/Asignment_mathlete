# This is the prototype of the application called "mathlete" the application solves mathematical problems for students
# age 10-13. I have been assigned a project to design and develop a computer program to help students age ten to
# thirteen to solve mathematical problems.

import math
import random


# Print out prompt messages to collect data
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
num3 = float(input("Enter a third number: "))

# print number1, number2 number3
print("You entered the following numbers:", num1, num2, num3)

# Arithmetic Operators
# Declare variable “result”
# Addition
result = num1 + num2
print(num1, "+", num2, "=", result)

# Subtraction & Division

result = (num1 - num2)
print(num1, "-", num2, "=", result)

# division
result = (num1 / num2)
print(num1, "/", num2, "=", result)

# multiply
result = num1 * num2
print(num1, "*", num2, "=", result)

# next step - even or odd
if (num1 % 2) == 0:
    print("{0} is Even number".format(num1))
else:
    print("{0} is Odd number".format(num1))

# next step - even or odd
if (num2 % 2) == 0:
    print("{0} is Even number".format(num2))
else:
    print("{0} is Odd number".format(num2))

# get absolute value for a number, create a variable for absolute_number
absolute_number = float(input("Enter a negative or positive number to get absolut value:"))

abs_value = abs(absolute_number)
print("This is the absolute value for", absolute_number, ":", abs_value)

# next step rounding to the nearest 10
# declare variable “nearest” = round number1 using round method
round_num = round(num1, -1)
print("nearest ten of ", num1, "=", round_num)
round_num2 = round(num2, -1)
print("nearest ten of ", num2, "=", round_num2)


# least common multiple - L.C.M. of two given number
# This function computes G.C.D.


def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# This function computes LCM
def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x, y)
    return lcm


print("The G.C.D. of, {0} and {1} is ".format(num1, num2), compute_gcd(num1, num2))
print("The L.C.M. of, {0} and {1} is".format(num1, num2), compute_lcm(num1, num2))


# divisibility rules
# method to check if the number could be divide by 6 or 3
def div_6_3(x):
    if (x % 6) == 0:
        print(x, "could be divided by 6 without a remainder.")
    elif (x % 3) == 0:
        print(x, "could be divided by 3 without a remainder.")
    else:
        print(x, "could not be divided by 3 or 6 without a remainder.")


# call the method div_6_3 check number1 and number 2
print(div_6_3(num1))
print(div_6_3(num2))


# Exponents and square roots
# exponents
# method to check a given number power of the second given number
def power(x, y):
    pow_result = math.pow(x, y)
    print("{0} power of {1} = ".format(x, y), pow_result)


# square roots
# method to check the square root of the given number
def square_route(x):
    sqrt_result = math.sqrt(x)
    print("Square route of", x, "=", sqrt_result)


# call exponents and square route methods
power(num1, num2)
power(num2, num1)
square_route(num1)
square_route(num2)


#
# Geometric Measurement
# Area of Square
def area(a, b):
    square_area = a * b
    print("Area of the square", a, "*", b, "=", square_area)


# Perimeter of Triangle
def perimeter(a, b, c):
    triangle_perimeter = a + b + c
    print("perimeter of the triangle is", a, "+", b, "+", c, "=", triangle_perimeter)


# Units of measurements
# km to miles (1 km = 0.6214 miles)
def miles(a):
    km_to_miles = a * 0.6214
    print(a, "km in miles is", km_to_miles)


# miles to km (1 mile is 1.6093 km)
def km(a):
    miles_to_km = a * 1.6093
    print(a, "miles in km is", miles_to_km)


# call measurement methods
area(num1, num2)
perimeter(num1, num2, num3)
miles(num1)
miles(num3)
km(num1)
km(num3)


# pythagoras theorem method
def pythagoras(a, b):
    theorem = math.pow(a, 2) + math.pow(b, 2)
    print("pythagoras theorem: c power 2 = {0} power 2 + {1} power 2 = ".format(a, b))
    c = math.sqrt(theorem)
    print("c = ", c)


pythagoras(num1, num2)


# Trigonometric Functions

def cosine(a):
    cosine_result = math.cos(math.radians(a))
    print("cosine of", a, "=", cosine_result)


def sinus(a):
    sinus_result = math.sin(math.radians(a))
    print("sinus of", a, "=", sinus_result)


def tangent(a):
    tangent_result = math.tan(math.radians(a))
    print("tangent of", a, "=", tangent_result)


cosine(num1)
sinus(num1)
tangent(num1)


# One-variable equations
# create variable z and assign a random integer from 1 to 100
z = random.randint(1, 100)
d = num1 * z + 3 * num2 + num3
print("{0} = {1} * z + 3 * {2} + {3}".format(d, num1, num2, num3))
e = int(input("Enter the number which would satisfies the equation:"))
if z == e:
    print("The answer is good.")
else:
    print("The answer is wrong.\nGood answer is " + str(z))
