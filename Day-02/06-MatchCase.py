# match case

x = int(input("Enter your number :- "))

match x:
  case 1:
    print("Enter number is 1")
    
  case 2:
    print("Enter number is 2")
    
  case 66:
    print("Enter number is 66")
    
  case _:
    print("Enter number is unknown")