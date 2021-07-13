list=[2,3,5,4,2,4,3]
index=0
a=[]
while index<(len(list)):
	if list[index] not in a:
		a.append(list[index])
	index=index+1
print(a)