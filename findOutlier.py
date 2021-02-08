def find_outlier(integers):
    dummy = [num%2 for num in integers]
    if sum(dummy) > 1:
        dummy = [not num for num in dummy]
    
    for i, x in enumerate(dummy):
        if x:
            return integers[i]
    
    return "No outliers"

myList = [21,17,15,3,61]
output = find_outlier(myList)
print(output)