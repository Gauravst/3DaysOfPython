# for loop

x = int(input("Enter your number :- "))

for i in range(x):
  
  if((i + 1) == 9):
    break
  
  if((i + 1) == 5):
    continue
  
  print(i + 1)

# y = (1, 45, 756, 9678, 33)
# for i in y:
#   print(i)