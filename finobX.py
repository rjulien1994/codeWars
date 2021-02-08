def countFib(n):
    count = len(str(n))
    if n == 1:
        return count
    else:
        return count + countFib(n-1)

print(countFib(100))
