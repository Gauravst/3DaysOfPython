# set and set methods
s = {2, 4, 24, 6, 7, 7, 7}
print(s)

s.pop()
print(s)

s.add(66)
print(s)

x = {5, 2, 88, 99}
z = s.union(x)
print(z)

a = s.intersection(x)
print(a)

s.clear()
print(s)

