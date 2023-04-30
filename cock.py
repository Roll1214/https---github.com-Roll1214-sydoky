# ar = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
# result = []
# resultt = []
# count = 0
# for i in ar:
#     i = str(i)
#     if i != '0':
#         result.append(i)
#     else:
#         count+=1
# result.extend([0]*count)
# for i in result:
#     i = int(i)
#     resultt.append(i)
# print(resultt)






def move_zeros(ar):
    result = []
    count = 0
    for i in ar:
        if i != 0:
            result.append(i)
        else:
            count+=1
    for i in range(count):
        result.append(0)
    return result
print(move_zeros([1,53, 22, 0, 2, 0, 2]))






