List=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(List):
    j=0
    multi=1
    while j<len(List[i]):
        multi=multi*List[i][j]
        j=j+1
    print(multi)
    i=i+1