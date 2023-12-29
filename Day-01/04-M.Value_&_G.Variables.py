# Assign Multiple values & Global Variables

# Assign Multiple values
x, y, z = "hello", "hi", "how"

print(x) #hello
print(y) #hi
print(z) #how

# Global Variables :- variables that are created outside of a function

a = 5

def myfun():  #Note: function on hold, baad m padenge
	print(a)

myfun()
print(a)


# Global Keyword

def myfun2():
	global b
	b = 67
	print(b)

myfun2()
print(b)