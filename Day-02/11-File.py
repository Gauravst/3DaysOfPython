# file I/O


# file writing
x = "My name is gaurav"

a = open("text.txt", "w")
a.write(x)
a.close()

with open("text2.txt", "w") as f:
	f.write(x)

# file reading
b = open("text.txt", "r")
r = b.read()
print(r)
b.close()

with open("text2.txt", "r") as g:
  r2 = g.read()
  print(r2)

# appanding to a file

c = open("text.txt", "a")
c.write("Hello how are you")
c.close()

with open("text2.txt", "a") as h:
  h.write("I Love you")
  h.close()