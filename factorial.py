def factorial(value):
    if value < 0:
         raise ValueError("Factorial is not defined for negative numbers.")
    
    elif value == 0 or value == 1:
         return 1
    
    elif value is str:
         raise TypeError("Factorial is not defined for strings")
    
    else:
         return value*factorial(value - 1)


