def mix(s1, s2):
    count = {l:[s1.count(l),s2.count(l)] for l in set(s1).union(set(s2)) if l >= 'a' and l <= 'z'}
    ordStr = sorted([[val[1]-val[0], max(val), key] for key, val in count.items() if max(val) > 1], key = lambda s: (-s[1], s[2]))
    output = []
    for w, m, l in ordStr:
        p = ''
        if w < 0:
            p += '1'
        elif w > 0:
            p += '2'
        else:
            p += '='
        p += ':'
        p += l*m
        output.append(p)

    return '/'.join(output)

print(mix("Are they here", "yes, they are here"))
#key = 'h'
#print(3*key)

#print({"Are they here".split()})