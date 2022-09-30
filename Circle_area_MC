import random
import math
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def MCunitballvolume(d,n):
    count = 0
    for _ in range(n):
        point = [random.random() for _ in range(d)]
        if sum(x*x for x in point) <= 1:
            count += 1
    return 2**d*(count/n)


def variance(l):
    return sum(x*x for x in l)/len(l)-(sum(l)/len(l))**2


# for n in [10, 100, 1000, 10000, 100000, 1000000]:
#     v = variance([MCunitballvolume(2,n) for _ in range(16)])
#     print('n =',n,'variance =',v,'n*variance =',v*n)

f = math.gamma
iter = 0
xprev = 0
fprev = f(xprev)
while True:
    xnext = xprev + (random.random()-0.5)
    fnext = f(next)
    if fnext < fprev:
        xprev, fprev = xnext, fnext
    iter += 1
    if iter%10000 ==0:
        print(xprev,fprev)
        
