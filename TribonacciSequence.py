def tribonacci(signature, n):
    if len(signature) < n:  #check if signutare is as long as required
        signature.append(sum(signature[-3:]))  #compute and append requested val
        return tribonacci(signature, n)
    else:
        return signature[:n]    #in case n = 0 returns empty array


print(tribonacci([2,1,1,2], 0))