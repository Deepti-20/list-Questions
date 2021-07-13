list1=[1,2,3,4]
list2=["deepti","durga","neha","rani"]
dic={}
i=0
while i<len(list1):
    # dic.update({list1[i]:list2[i]})
    dic[list1[i]]=list2[i]
    i=i+1
print(dic)