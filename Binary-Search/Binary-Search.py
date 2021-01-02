def binary_search(alist, target):
   guess = 0
   min_num = 0
   max_num = len(alist)-1
   while(max_num >= min_num):
      guess = (min_num + max_num) // 2
      if(alist[guess] == target):
         print(str(alist[guess]) + " found at index: " + str(guess))
         return guess
      elif(alist[guess] < target):
         min_num = guess + 1
      else:
         max_num = guess - 1
   return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
ans = binary_search(primes, 67)
print(ans)