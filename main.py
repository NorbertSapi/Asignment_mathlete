# This is the prototype of the application called "mathlete" the application solves mathematical problems for student
# age 10-13. I have been assigned a project to design and develop a computer program to help students age ten to
# thirteen to solve mathematical problems.

import math

# get user input
age = int(input("How old are you? "))
print(age)

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))

if age == 10:
    # 1.1 Arithmetic Operators
    result = num1 + num2
    print("num1 + num2 = " + str(result))

    # subtract
    result = num1 - num2
    print("num1 - num2 = " + str(result))

    # divide
    result = num1 / num2
    print("num1 / num2 = " + str(result))

    # multiply
    result = num1 * num2
    print("num1 * num2 = " + str(result))

    # 1.2 Place values and number sense:
    # even or odd
    if num1 % 2 == 0:
        print('num1 is even number')
    else:
        print("num1 is odd number")

    # even or odd
    if num2 % 2 == 0:
        print('num2 is even number')
    else:
        print("num2 is odd number")

    # rounding to the nearest 10
    nearest = round(num1, -1)
    print(" The nearest 10 to {0} is {1}".format(num1, nearest))

    # 1.3 Number Theory
    # greatest common factor
    greatest_common_factor = math.gcd(int(num1), int(num2))
    print("greatest common factor of " + str(num1) + " and " + str(num2) + " is " + str(greatest_common_factor))

    # least common multiple
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    least_common_multiple = lcm(int(num1), int(num2))
    print("least common multiple of {0} and {1} is ".format(num1, num2))

    # continue the if statement for the age group
    # age 11: use power function
elif age == 11:
    result = math.pow(num1, num2)
    print("{0} power {1} is {2}. ".format(num1, num2, result))
    #
    # age 12: use square root function
elif age == 12:
    # count square root
    result1 = math.sqrt(num1)
    result2 = math.sqrt(num2)
    print(result1)
    print(result2)
    #
    # age 13: use
elif age == 13:
    result = math.sin(math.radians(num1))
    print("Sinus {0} is {1}.".format(num1, result))
else:
    # solve other input cases
    print("You're in a different age group. "
          "We might offer age relevant mathematical functions in the future version. "
          "Thank you!")
