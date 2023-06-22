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


