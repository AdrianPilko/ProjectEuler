# script to solve project euler problem 12

maxFactor = 0

def factor_number(x):
    #print ("The factors of",x," are")
    numberOfFactors = 0;
    for i in range(1,x+1):
        if x % i == 0:
            #print(i)
            numberOfFactors+=1
    return numberOfFactors


def find_triagnle_number(x):
    tri = 0
    global maxFactor
    for i in range(1,x+1):
        tri = i + tri
    factors = factor_number(tri)
    if factors>maxFactor:
        maxFactor = factors
        print ("The ",x," triangle number is ", tri," has current highest ",factors," factors")
    if maxFactor>500:
        print ("Found over 500 factors for the triangle number ",x," was ",factors)
        exit()
    

x = 0
for x in iter(lambda: x+1, -1):
    find_triagnle_number(x)
    
