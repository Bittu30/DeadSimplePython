# this is chapter 5
# this chapter is too heavy will do after finish two books
# chuck and allen downey


# function call
print(type(32))

# built in function

print(max('hello world'))
print(min('hello world'))
print(len('hello world'))

# Type conversion functions

int('32')
float(32)
str(32)

# Math Functions

import math

print(math)

radians = 0.7
height = math.sin(radians)
print(height)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
print(math.sqrt(2) / 2.0)

# Random Numbers

import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))
print(random.randint(5, 10))


# we can get random number from dstr like Gamma, exponentail,gamma
# few more

# Adding new functions

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print('I sleep all night and I work all day.')


print(print_lyrics)
print(type(print_lyrics))

print_lyrics()


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# Flow of execution

# Parameters and arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('spam')
print_twice(17)

print_twice('Spam ' * 4)

# Fruitful functions and void functions

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2


def addtwo(a, b):
    added = a + b
    return added


z = addtwo(3, 5)
print(z)

# chapter 5 Iteration

x = 0
x = x + 1
print(x)

# while

n = 5
while n > 5:
    print(n)
    n = n - 1
print('Blastoff!')

# Finishing iteration with continue

friends=['Joseph','Glenn','Sally']
for friend in friends:
    print('Happy New Year:',friend)
print('Done!')

#Loop Pattern

count=0
total=0
for itervar in [3,42,56,77,88]:
    count=count+1
    total=total+itervar
print('Count: ',count)
print('total: ',total)