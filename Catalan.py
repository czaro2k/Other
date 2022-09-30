def memoize(f):
    memo = {}
    def helper(*x):
        if x not in memo:            
            memo[x] = f(*x)
        return memo[x]
    return helper


def Cat(n):
    M = []
    if n == 0:
        return 1
    elif n > 0:
        for i in range(n):
            M.append(Cat(i)*Cat(n-1-i))
    return sum(M)
Cat = memoize(Cat)


def Cat2(n): 
    if n <= 1 : 
        return 1 
    liczba = 0 
    for i in range(n):   
        liczba += Cat2(i)*Cat2(n-i-1) 
    return liczba
Cat2 = memoize(Cat2)



@memoize
def Cat3(n): 
  if n<= 1:
      return 1
  else:
      return sum(Cat3(i)*Cat3(n-i-1) for i in range(n))
  
    
def Cat4(n):
   if (n == 0 or n == 1):
      return 1
   Cat4 = [0 for i in range(n + 1)]
   Cat4[0] = 1
   Cat4[1] = 1
   for i in range(2, n + 1):
      Cat4[i] = 0
      for j in range(i):
         Cat4[i] = Cat4[i] + Cat4[j] * Cat4[i-j-1]
   return Cat4[n]

for i in range(100):
    print(i, " ", Cat4(i))
    
