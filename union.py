arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
list=[]
list.extend(arr1)
i=0
while i<len(arr2):
    if arr2[i] not in list:
        list.append(arr2[i])
    i=i+1
print(list)

