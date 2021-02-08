
def integer_right_triangles(p):
    C1 = [i for i in range(1, int(p/(2+2**0.5)))]   # max length when c1 = c2
    C2 = [0.5*(p-c1-(c1*c1)/(p-c1)) for c1 in C1]    #by theorem
    output = [[c1,c2,p-c1-c2] for c1, c2 in zip(C1,C2) if c2%1 == 0]
    return output


result = integer_right_triangles(386784)
exp = [[12240, 187072, 187472], [21488, 182016, 183280], [22752, 181305, 182727], [34272, 174590, 177922], [42976, 169218, 174590], [49770, 164832, 172182], [53856, 162108, 170820], [68493, 151776, 166515], [87216, 137088, 162480], [96696, 128928, 161160], [112812, 113760, 160212]]

e = [x for x in result if x not in exp][0]

print(e[0]**2 + e[1]**2 == e[2]**2)
print(e[0] + e[1] + e[2] == 386784)

#print(result)