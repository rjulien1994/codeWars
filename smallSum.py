import math

#method 1
def solution(a):
    if len(a) == 1:
        return a[0]
    GDC = a[0]
    for n in a[1:]:
        GDC = math.gcd(GDC, n)

    return int(GDC*len(a))

#method 2
def solution1(a):
    setA = set(a)
    while len(setA) > 1:
        maxVal = max(setA)
        setA.remove(maxVal)
        setA.add(maxVal-max(setA))

    return list(setA)[0]*len(a)

#method 3 -> too slow
def solution2(a):
    maxVal = max(a)
    while maxVal != min(a):
        smallerVal = max([x for x in a if x != maxVal])
        a = [x if x != maxVal else x-smallerVal for x in a]
        maxVal = max(a)
    return sum(a)

print(solution2([6, 9, 21]))
