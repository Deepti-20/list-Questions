list1=[[8,10,9],[7,5,4],[11,20,21]]
max=0
i=0
while i<len(list1):
    j=0
    while j<len(list1[i]):
        if list1[i][j]>max:
            max=list1[i][j]
        j=j+1
    i=i+1
    print(max)