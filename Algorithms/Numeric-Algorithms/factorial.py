"""Calculates the factorial of a given number"""

def factorial(n):
   if n < 2:
      return 1
   fact = 1
   for i in range(2, n+1):
      fact *= i
   return fact

print(factorial(5))