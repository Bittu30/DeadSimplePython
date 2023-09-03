# name=input("what is your name?")
# print("hello "+name)

message = "Hello,world!"
print(message)

# The Importance of Nesting

name = "Jason"

if name != "":
    message = "Hello, " + name + "!"
    print(message)
print("I am computer.")

raining = True
hailing = False

if raining:
    if hailing:
        print("Nope")
    else:
        print("Umbrella Time")

raining = True

if raining:
    pass

# comments and DocStrings

# this is comment
print("Hello World")

print("How are you")  # inline comment


# here is another comment
# you get the idea

def make_tea():
    """will produce the concocation almost,
    but not entirely like tea
    """
    pass


print(make_tea.__doc__)

# this is the constant you can change this but will be flag
# be linter
INTEREST_RATE = 5.00

# operators,  these will be unary operators
print(-42)
print(abs(-42))

c = divmod(52, 17)
print(c)

# the math module

import math

print(math.pi)
print(math.tau)

print(math.inf)
print(math.nan)

distance_ft = 65
angle_def = 74

angle_rad = math.radians(angle_def)
height_ft = distance_ft * math.tan(angle_rad)
height_ft = round(height_ft, 2)
print(height_ft)

spam = True
eggs = False
potatoes = None

if eggs is spam:
    print("This won't work")

# the walrus operator

if (eggs := 7 + 5) == 12:
    print("We have one dozen eggs")
print(eggs)

# Strings

danger = "Cuidado llamas!"

print(danger)

quote = 'Shout, "Cuidado llamas!"'

print(quote)

# raw strings

print(r"I love backlashes: \ Aren't they cool?")
# Always use raw strings for regular expression patterns

# f-strings

int_stock = 0
print(f"This cheese shop has {int_stock} types of cheese")

print(f"{5+5=}")

answer = 42
print(f"{answer}")

# Template Strings

from string import Template

s = Template("$greeting,$user!")

print(s.substitute(greeting="Hi", user="Jason"))

# A Note on String Concatenation

greeting = "Hello"
name = "Jason"

message = "".join((greeting, ", ", name, "!"))
print(message)


# join is faster in concatenation

# Functions

# Function are first class citizens and you can use them
# like any other object

def tell_joke(joke_type):
    pass


print(tell_joke("funny"))


# Classes and Objects

class Joke:
    pass


import sys

print(sys.path)

# The immutable truth

eggs = 12
carton = eggs
print(eggs is carton)
eggs += 1
print(eggs is carton)
print(eggs)
print(carton)

temps = [87, 76, 79]

highs = temps
print(temps is highs)
temps += [81]
print(temps is highs)
print(highs)
print(temps)


# passing by assignment
def greet(person):
    print(f"Hello, {person}.")


my_name = "Jason"
greet(my_name)


# this func has side effects
def find_lowest(temp):
    temp.sort()
    print(temp[0])


temps = [85, 76, 79, 72, 81]
find_lowest(temps)
print(temps)

# coercion and conversion

print(42.5)
x = 5 + 1.5
y = 5 + True

life_universe_everything = "42"

answer = float(life_universe_everything)

print(type(answer))

print(answer)

# collection and References

