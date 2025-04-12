# module a.star
def f(x, list=[]):
    list.append(x)
    return list

print(f(4, [1,2,3,4]))
print(f(1))
print(f(2))
print(f(3))


