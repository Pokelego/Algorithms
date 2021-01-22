"""Calculates the greatest common denominator of two values"""

def GCD(n, m):
   if n == 0:
      return m
   return GCD(m % n, n)
