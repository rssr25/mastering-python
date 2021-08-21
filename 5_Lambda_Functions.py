def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85

#using lambda
func2 = lambda x: x+5
print(func2(7))
print(func(7))

print(func(1))


func3 = lambda x, y=4: x+5
print(func3(4))

#with map and filter
a = [i for i in range(1, 11)]
print(list(map(lambda x : x+5, a)))
print(list(filter(lambda x: x%2 == 0, a)))