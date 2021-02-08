def array_diff(a, b):
    result = [val for val in a if val not in b]
    return result

print(array_diff([1,2], [1]))