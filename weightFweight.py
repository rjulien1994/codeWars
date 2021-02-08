#method 1
def order_weight(strng):
    score = []
    strng = strng.split(" ")
    for n in strng:
        digits = [int(d) for d in str(n)]
        score.append(sum(digits))

    output = " ".join([x for y,x in sorted(zip(score,strng))])
    return output

#method 2
def order_weight(strng):
    strng = strng.split(" ")
    score = [sum([int(d) for d in n]) for n in strng]
    output = " ".join([x for y,x in sorted(zip(score,strng))])    #place the order nums into a string
    return output

#method 3
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
#join(sort based on (sort based on num string, compute score))

result = order_weight("103 123 4444 99 2000")
print(result)