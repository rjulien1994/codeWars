def isPrime(num):
    if num%2 == 0:
        return False
    for n in range(3, int(num**0.5)+1, 2):
        if num%n == 0:
            return False
    return True

def gap(g, m, n):
    Fprime = -g
    for val in range(m+1 - m%2,n+1,2):
        if isPrime(val):
            if val - Fprime == g: return [Fprime, val]
            Fprime = val
    return None


print(gap(2,100,110))