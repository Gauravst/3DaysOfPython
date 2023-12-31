# oops classes and object

class person:
  
  def __init__(self, name, age, subject):
    self.name = name
    self.age = age
    self.subject = subject
    
p1 = person('gaurav', 44, 'computer')
p2 = person('ram', 64, 'math')
p3 = person('mohit', 94, 'hindi')

print(p1.name)
print(p1.age)
print(p1.subject)

print(p2.name)
print(p2.age)
print(p2.subject)

print(p3.name)
print(p3.age)
print(p3.subject)
