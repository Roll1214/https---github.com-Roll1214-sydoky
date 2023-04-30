grid = [[3,6,2,     5,8,4,      9,1,7],
        [5,4,7,     2,1,9,      3,6,8],
        [8,9,1,     7,6,3,      2,4,5],

        [2,7,8,     6,4,5,      1,3,9],
        [1,5,9,     3,2,7,      4,8,6],
        [6,3,4,     8,9,1,      5,7,2],

        [7,8,5,     1,3,2,      6,9,4],
        [4,1,6,     9,5,8,      7,2,3],
        [9,2,3,     4,7,6,      8,5,1]]
# range1 = 0
# range2 = 3
# count= 0
# for i in range(3):
#     for i in range(3):
#         ar2 = []
#         for i in range(range1,range2):
#             for j in range(range1,range2):
#                 ar2.append(grid[j][count])
#                 if len(ar2)%3==0:
#                     count+=1
#         print(ar2)                                ПРОВЕРКА 3X3 БЛОКА
#         for i in ar2:
#             if ar2.count(i)>1:
#                 print(True)
#                 break
#             else:
#                 print(False)
#     count = 0
#     range1+= 3
#     range2+= 3


# for lines in range(9): 
#     for element in range(9):
#         if grid[lines].count(grid[lines][element])>1: ГОТОВАЯ ПРОВЕРКА ДЛЯ СТРОК
#             print(True)


# for k in range(9):
#     ar = []
#     for i in range(9):
#         ar.append(grid[i][k])         ГОТОВАЯ ПРОВЕРКА ДЛЯ СТОЛБИКОВ
#     for i in ar:                     
#         if ar.count(i)>1:
#             print(True)






       

            
            

# def validate(a):
#     print(grid[0])

# validate(a)

