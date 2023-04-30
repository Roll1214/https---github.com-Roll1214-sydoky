def count(s):
    r = 0
    s = s.lower()
    result = {}
    for i in s:
        if i in result.keys():
            result[i]+=1
        else:
            result[i]=1
    for i in result.values():
        if i > 1:
            r+=1
    return r
    
print(count('Indivisibilities'))
      