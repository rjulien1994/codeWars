def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))    #max(value wanted, get index of max elem)

print(high('man i need a taxi taxi to ubud'))