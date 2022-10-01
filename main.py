                                            # PROGRAMMING WITH MOSH    Python for Beginners - Learn Python in 1 Hour
                                            # https://www.youtube.com/watch?v=kqtD5dpn9C8

# 1. basic printing statements
first_name = "John Smith"
age = 20
new_patient = True

print("Age is " + str(age))  # using str() we can concatenate in a string
print(new_patient)  # using str() we can concatenate in a string
print("First Name is " + first_name + " age is " + str(age) + " is a new patient boo value " + str(new_patient))

# 2. taking input from user

name = input("Heyy!,What's your name? ")
print(name)
birth_year = input("Enter your birth year ")  # input returns always strings
age_cal = int(birth_year) - 1995  # typecasting to int
print(age_cal)

# Ex - Calculator Program
first = float(input("Enter first number "))  # directly converting input str to float
second = float(input("Enter second number "))
sum = first + second
print(sum)

# 3.STRING MANIPULATIONS -important String treated like an object and every function creates a new string object,
# thus the existing string variable remain same.

first_name = "Python Is Love"
print(first_name.upper())  # new String object gets created for every string manipulation
print(first_name)  # existing one remains same

print(first_name.find("P"))
print("P" in first_name)  # returns True/ false, another way to search characters

# 4. Arithmetic Operators

print(10 / 3)  # regular division 3.333
print(10 // 3)  # returns 3
print(10 % 3)  # returns 1 (modulo)
print(10 * 3)  # regular multiplication
print(10 ** 3)  # regular exponential i.e 1000

x = 10
x += 3  # Same as x = x+3 (Augmented Operator)
x = 2 == 3
x = 2 != 3

price = 25
print(price > 10 and price < 40)  # and operation
print(10 < price < 40)  # simpler way
print(price > 10 or price < 20)
print(not price > 10)

# 5. Conditional Operator

# Example - weight conversion
weight = float(input("Enter your weight "))
unit = input("Enter (K)g or (L)bs ")

res = 0
if unit.upper() == 'K':
    res = weight * 2.2
    print("Converted Result is " + str(res) + "Lb")
elif unit.upper() == 'L':
    res = weight / 2.2
    print("Converted Result is " + str(res) + "Kg")
print("end of condition")

# 6. while loop
i = 1
while i <= 1_000:  # better readability for 1000
    print(i)
    i = i + 1
print("End of while")

#   Interesting * design using while

i = 1
while i <= 5:
    print(i * '*')  # Unlike + concatenation, with * we can directly concatenate and it will get multiplied to
    # give pattern
    i += 1

# 7. List

names = ["Treena", "Raj", "Dey"]
print(names[-2])
names[0] = "Tre"
print(names)

# List has its own set of methods, similar to string, but List  is mutable.
names.insert(0, False)  # can insert values of any type, o/p [ False,Tre, Raj, Dey]

for item in names:
    print(item)

# 8. range function - quite interesting:
nums = range(6)  # (0-5)
nums = range(5, 10)  # (5-10)
nums = range(5, 10, 2)  # (5-10, increment by step of 2 )

for num in nums:
    print(num)
# directly using range in the for loop
for num in range(5, 10, 3):
    print(num)

# TUPLES - Immutable list kind objects, only String and tuples are immutable, no insert/ deletion i.e modification
# type functions are available

tuple_val = ("Treena", "raj", "dey")  # () instead of []
for val in tuple_val:
    print(val)
# only below two tuple methods exists and one add magic functions- discussed in advanced
tuple_val.count("Treena")  # number of times a particular character appears
tuple_val.index("Treena")  # first index when the given char appears
