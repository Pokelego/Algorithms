"""Converts a base 10 number to its binary equivalent"""

def toBinary(n):
   out = []
   while n > 0:
      out.append(n % 2)
      n  //= 2

   out.reverse()
   return ''.join(map(str, out))
