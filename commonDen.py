import math

def convertFracts(lst):
    GCD = 1
    for _, d in lst:
        GCD = GCD*d//math.gcd(GCD,d)
    return [[n*GCD//d,GCD] for n,d in lst]

#print(convertFracts([[1, 2], [1, 3], [1, 4]]))
print(1.56+(1-1.56%1))