#map function takes two parameters: a function and a list
li = [i for i in range(1, 11)]
def func(x):
    return x**x

#conventional
newList = []

for i in li:
    newList.append(func(i))

print(newList)


#using map function
print(list(map(func, li)))

#or list comprehension
print([func(i) for i in li])
