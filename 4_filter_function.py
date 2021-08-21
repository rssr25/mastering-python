def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [i for i in range(1, 11)]

b = list(filter(isOdd, a))
print(b)
print(list(map(isOdd, a)))

print(list(map(add7, filter(isOdd, a))))

#filter uses a function that gives a true/false value