
list1=[[2, 3, 4], [3, -4, -5, 6], [7, 8, 9, 10, 11], [-12, -13, -14]]
i=0
while i<len(list1):
    j=0
    k=1
    while j<len(list1[i]):
        print(list1[i][k])
        if list1[j][i]<list1[i][k]:
            # print(list1[i][j])
            k=k+1
        j=j+1
    i=i+1

