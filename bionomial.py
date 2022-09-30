 def memoize(f):
    memo = {}
    def helper(*x):
        if x not in memo:            
            memo[x] = f(*x)
        return memo[x]
    return helper

@memoize
def catalan_number(n): 
  if n<= 1:
      return 1
  else:
      return sum(catalan_number(i)*catalan_number(n-i-1) for i in range(n))

@memoize
def dwumian(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return  dwumian(n-1,k-1)+dwumian(n-1,k)
        
print(dwumian(1000, 50))

#test czy liczby Catalana zgadzają się ze wzorem C(n) = 1/(n+1) (2n, n)
print(catalan_number(300))
print(dwumian(600,300)//301)

n=3;
btab = [[1 for i in range(n)] for j in range(n)]

for i in range(1,n):
    for j in range(1,n):
        btab[i][j] = btab[i-1][j-1]+btab[i-1][j]
        
m,n=3,4;
btab = [[1 for j in range(n)] for i in range(m)]

def binomial(n,k):
    btab = [[1 for j in range(k+1)] for i in range(n-k+1)]
    for i in range(1,n-k+1):
        for j in range(1,k+1):
            btab[i][j] = btab[i-1][j]+btab[i][j-1]
    return btab[n-k][k]

print(dwumian(150,122))
print(binomial(150,122))
