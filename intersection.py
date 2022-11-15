def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)


# arr1 = [1, 2, 4, 5, 6]
# arr2 = [2, 3, 5, 7]
# m = len(arr1)
# n = len(arr2)
# i=0
# list=[]
# union=0
# while i<(m):
#     if arr1[i]  not in arr2:
#         list.append(arr1[i])
#     if arr2[i] in arr1:
#         list.append(arr2[i])
#     else:
#         list.append(arr2[i])
#         i=i+1
# union=list.sort()
# print(list)
# j=0
# while j < n:
#     if arr1[i] < arr2[j]:
#         i += 1
#     elif arr2[j] < arr1[i]:
#         j+= 1
#     else:
#         print(arr2[j],end=" ")
#         j += 1