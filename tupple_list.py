# a=(243543)
# output= [3,4,5,3,4,2]

a=(243543)
list1=list(str(a))
list2=[]
i=-1
while i>=(-len(list1)):
    list2.append(int(list1[i]))
    i=i-1
print(list2)