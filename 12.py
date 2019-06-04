# script to solve project euler problem 12
import time
import math 
def v(x):
    numberOfFactors = 0
    for i in range(1,x+1):
        if x % i == 0:
            numberOfFactors+=1
    return numberOfFactors

def factor_number(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors


def tri(x):
    num = x*((x+1)/2)
    return int(num)
    

def find_tris(x):
    for i in range (1, x, 1):
        start=time.time()
        tr = tri(i)
        triTime = (time.time() - start)

        start=time.time()
        facts = factor_number(tr)
        factTime = (time.time() - start)

        if facts >=400:
            print("found triangle number ", tr, " with ", facts, " factors, times: tri=",triTime, " fac=", factTime);
            if facts >=500:
                exit()
                
if tri(7) != 28:
    print("error did not pass test, tr4(7) should be 28, we got ", tri(7));
    exit();
if factor_number(tri(7)) != 6:
    print("error did not pass test, number of factors of tri(7) = 28 = 6, we got ", factor_number(tri(7)))
    exit();

find_tris(10000000000);    
