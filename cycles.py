ar = [2, 4, 0, 100, 4, 11, 2602, 36]
def find_outlier(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            even += i + 1
        else:
            odd += i + 1
    if(even > len(arr)):
        return arr[odd - 1]
    return arr[even - 1]




cOdd = 0
cEven = 0
for i in ar:
    if i%2 == 0:
        cEven+=1
    else:
        cOdd+=1
if cEven>cOdd:
    for i in ar:
        if i%2 == 1:
            print(i)
if cOdd>cEven:
    for i in ar:
        if i%2 == 0:
            print(i)

    
