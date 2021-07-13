num1=int(input("enter any no."))
num=[]
i=0
while i<=num1:
	num2=int(input("enter any no."))
	num.append(num2)
	i=i+1
print(num)
a=0
while a<len(num):
	j=0
	while j<a:
		if num[a]<num[j]:
			b=num[a]
			num[a]=num[j]
			num[j]=b
		j=j+1
	a=a+1
print(num)