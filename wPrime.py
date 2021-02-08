import math

def an(n):
    output = [7]
    for i in range(2, n+1):
        output.append(output[i-2] + math.gcd(i, output[i-2]))
    return output

def gn(n):
    aS = an(n)
    output = [1]
    for i in range(1,len(aS)):
        output.append(aS[i]-aS[i-1])
    return output

def count_ones(n):
    return gn(n).count(1)

def p(n):
    elems = set()
    return [x for x in gn(n) if not (x in elems or elems.add(x))]

def max_pn(n):
    return max(p(n))

def anOver(n):
    return [val for val, cond in A, G if conf != 1]


def an_over_average(n):
    pass

print(gn(8))
print(p(8))