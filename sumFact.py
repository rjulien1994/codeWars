
#method 1
def sumFact(n, facts=[3,5]):
    N = range(2,n)  #n is not part of range
    multiples = [x for x in N if any([True for f in facts if x%f == 0])]
    return sum(multiples)

#method 2
def sumFact2(n, facts=[3,5]):
    multiples = {item for f in facts for item in range(f,n,f)}  #make it a set to avoid duplicates
    return sum(multiples)

#print(sumFact(5))   #--> sum(2,4)
#print(sumFact(10))   #--> sum(2,4,5,6,8)
#print(sumFact(20,[3,5]))   #--> sum(2,4,5,6,8)
print(sumFact2(5))

for target in range(2,100):
    print(sumFact2(target) == sumFact(target))