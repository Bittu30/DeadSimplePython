# this is charles_severance chapter 6 and chapter 7

fruit = 'banana'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

# getting the length of a string using len

fruit = 'banana'
print(fruit)

last = fruit[len(fruit) - 1]
print(last)

for char in fruit:
    print(char)

# String slices

s = 'Monty Python'
print(s[0:5])

print(s[6:12])

fruit = 'banana'
print(fruit[:3])

print(fruit[3:])

print(fruit[:])

# strings are immutable
greeting = 'Hello World!'

new_greeting = 'J' + greeting[1:]
print(new_greeting)

# looping and counting

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


def count(string, word):
    count = 0
    for letter in string:
        if letter == word:
            count = count + 1
    print(count)


count('banana', 'a')

print('a' in 'banana')

print('seed' in 'banana')

# strings methods

stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))

word = 'banana'
index = word.find('a')
print(index)

line = '  here we go  '
print(line.strip())

line = 'Have a nice day'
print(line.startswith('h'))

print(line.lower().startswith('h'))

print(word.count('a'))

# Parsing strings

data = 'From stephen.marquard@uct.ac.za Sat Jan'

atpos = data.find('@')
sppos = data.find(' ', 21)

host = data[atpos + 1:sppos]
print(host)

# Format operator

subnet = 'X-DSPAM-Confidence:0.8475'

atpos = subnet.find(':')
print(atpos)
sppos = subnet.find(' ', 18)

float_num = float(subnet[atpos + 1:sppos])
print(float_num)

# this is new chapter 7

# Files

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print("Line Count:", count)

fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(len(inp[:20]))

# seaching with files

fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)

fname=input('Enter the file name:')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count, 'subject line in',fname)

# writing files

fout=open('output.txt','w')
line1="This is here in the wattle.\n"
fout.write(line1)
line2='the emblem of our land.\n'
fout.write(line2)
fout.close()




