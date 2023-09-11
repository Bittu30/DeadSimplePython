# A list is a sequence

cheese = ['Chedder', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []

print(cheese, numbers, empty)

# list are mutable

print(cheese[0])
numbers = [17, 123]
numbers[1] = 3
print(numbers)
print('Edam' in cheese)

# traversing a list

for c in cheese:
    print(c)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])

for x in empty:
    print("This never happens.")

# List operations

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print([0] * 4)
print([1, 2, 3] * 3)

# List Slices
t = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(t[1:3])
print(t[:4])
print(t[3:])

# List methods
t=['a','b','c']
t.append('d')
print(t)

t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)

#list and functions

nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total=0
count=0

while (True):
    inp= input('Enter a number:')
    if inp=='done':break
    value =float(inp)
    total=total+value
    count=count+1
average=total/count
print('Average:',average)