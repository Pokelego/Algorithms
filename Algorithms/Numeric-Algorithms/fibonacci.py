"""Calculates the Fibonacci sequence of a given number"""
mem_fib = {0:0, 1:1}


def fib(n):
   if n not in mem_fib:
      mem_fib[n] = fib(n-1) + fib(n-2)
   return mem_fib[n]

