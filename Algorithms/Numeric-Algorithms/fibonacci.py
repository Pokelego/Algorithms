"""Calculates the Fibonacci sequence of a given number"""
memFib = {0:0, 1:1}


def fib(n):
   if n not in memFib:
      memFib[n] = fib(n-1) + fib(n-2)
   return memFib[n]

