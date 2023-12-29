# Strings and String Methods

x = "Hello"
y = 'hello'

print(x)
print(y)

# multiline string

z = """
Hi, my name is
Gaurav
Singh
Tangariya
"""
print(z)

# looping string
for i in x:
	print(i)

# string length
print("length of x is :", len(x))

# check string - present in string or not
print("He Present in x :- ", "He" in x) #true
print("He Present in x :- ", "He" not in x) #false

# slicing string
a = "Gaurav"
print(a[2:5]) #ura, Index 2 se Index 4(5-1) tk 
print(a[:5]) #Gaura, start se Index 4(5-1) tk
print(a[2:]) #urav, Index 2 se end tk
print(a[-5:-2]) #aur, Index -5 se -3(-2-1) tk, note -1 is last character(v) , -2 = a


# modify string
w = "Name"
g = "            hello  "

print(w) #Name
print(w.upper()) #NAME
print(w.lower()) #name
print(g) #            hello  
print(g.strip()) #hello

# replace string
print(w.replace("N", "H"))

# Split
v = "hello,world"
print(v.split(","))

# string concatenation
k = "Love "
l = "You"
m = k + l
print("k + l = m is :", m)

# format string 
name = "gaurav"
age = 22

info = "I am {} year old"
print(info.format(age))

info2 = "I am {1} year old and my name is {0}"
print(info2.format(name, age))

# escape characters in string

fa = "Gaurav\'hello heloo"
fb = "Gaurav\n'hello heloo"
fc = "Gaurav\\'hello heloo"
fd = "Gaurav\b'hello heloo"
fe = "Gaurav\t'hello heloo"
ff = "Gaurav\f'hello heloo"
fg = "Gaurav\000'hello heloo"
fh = "Gaurav\x32'hello heloo"

print(fa)
print(fb)
print(fc)
print(fd)
print(fe)
print(ff)
print(fg)
print(fh)




