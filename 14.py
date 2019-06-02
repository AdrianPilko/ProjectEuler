# script to solve project euler problem 14
# find longest collatz sequence starting n < 1000000
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
import time
 
start = time.time()

def evenRule(n):
    return (n / 2)

def oddRule(n):
    return ((3 * n) + 1)

endn = 1000000
print("Collatz sequence finder")
highest = []
highest.append(0)
highest.append(0)

for n in range(1, endn):
    term = n
    count = 1;
    ##print("start=",term)
    ##print (term,", ", end='')
    while term > 1:
        count+=1
        if term % 2 == 0: ## n is even
            term = evenRule(term)
        else:
            term = oddRule(term)
        #print (term,", ", end='')
    #print("")
    if (count > highest[0]):
        highest[0] = count
        highest[1] = n

print (highest[0], " ", highest[1])
elapsed = (time.time() - start)
print("elapsed time=",elapsed)
print("END")
