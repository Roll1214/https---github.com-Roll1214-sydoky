#Entry(вхождение) of an element into a set(множество)
# s = 'set'
# item in s 
# checks if an element is in a set


#Slice 
#copy part of iterable
#s[start:end:step]

#filter
#filter(def,range)

#localDef
#lambda create a def with local var 
#lambda i: action

#STR.lower() and STR.upper()
#STR.lower() - f which decrease size of all letters of the string
#STR.upper() - f which increase size of all letters of the string

# ' '.join(str) - put space between str
# ''.join(str) - sticks together str
# 'cock'.join(str) - put "cock" between str

#% // 
#x=35
#x%10 = 5
#x//10 = 3

#Split a string into a list where each word is a list item
#x.split()

#map(func iter)

#isdigit - str==int

#Double SPACE ' '.join(str.split(' '))

#function var.count(arg) проверяет сколько раз в массиве встречается аргумент
#example a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]  print(a.count(20)) выведет 2, число 20 встречается 2 раза в массиве

#Counter функция которая, отображает число и сколько раз оно встретилось в массиве, это словарь
#example
#from collections import Counter
#a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
#a = Counter(a)
#print(a)
#выводит Counter({5: 3, 20: 2, 1: 2, -1: 2, 2: 2, -2: 2, 3: 2, 4: 2})




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
