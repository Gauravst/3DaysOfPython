# list and list methods

x = ['apple', 'apple', 'cherry', 'banana']
print(x)
print(type(x))

x.remove('apple')
print(x)

print(x.count('apple'))

y = [2, 44, 5, 12]
y.sort()
print(y)

x.sort()
print(x)

y.pop()
print(y)

y.append("Hello")
print(y)

z = y.copy()
print("z is :", z)

z.extend(["i", "love", "you"])
print("extend z is :-", z)