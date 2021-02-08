#Method 1
def getPrimes(maxVal):
    myList = [2]
    for num in range(3, maxVal+1):
        prime = True
        for i in myList:
            if num % i == 0:
                prime = False
                break
        if prime:
            myList.append(num)
    return myList


def sum_for_list(lst):
    output = []
    for i in getPrimes(max([abs(val) for val in lst])):
        divVal = [x for x in lst if x%i == 0]
        if len(divVal) != 0:
            output.append([i, sum(divVal)])
    
    return output


# method 
def sum_for_list(lst):
    #fetch all dividants and store it in a set to avoid duplicates
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}    
    #Goes thru the dividants and finds the prime numbers (a single false value in array makes the whole condition false)
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    #sums and returns the values that are divisible by remaining prime factors
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

print(sum_for_list([64, -127, -179, -20, -162, 116, -114, -108, -174, -48, 91, -179, -171, -35]))
#print(getPrimes(100))