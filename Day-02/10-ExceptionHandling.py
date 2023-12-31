# exception handling

try:
  x = int(input("Enter your number :-"))
  print(f"Your number is :-{x}")
  
except Exception as e:
  print("some error  occurred :- ", e)