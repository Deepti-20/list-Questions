
list1=[[2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
list2=[]
while i<len(list1):
    max=0
    j=0
    while j<len(list1[i]):
        if list1[i][j]>max :
            max=(list1[i][j])
        j=j+1
    list2.append(max)
    i=i+1
print(list2)


