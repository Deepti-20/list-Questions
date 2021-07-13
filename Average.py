elements=[23,14,56,12,19,9,15,25,31,42,43]
index=0
num=[]
num1=[]
sum=0
sum1=0
sum3=0
count3=0
count1=0
count2=0
while index <len(elements):
	if elements[index]%2==0:
		num.append(elements[index])
		sum=sum+elements[index]
		count1=count1+1
	else:
		num1.append(elements[index])
		sum1=sum1+(elements[index])
		count2=count2+1
	count3=count3+1
	sum3=sum3+elements[index]
	average3=sum3/count3
	index=index+1
average=sum/count1
average1=sum1/count2
average3=sum3/count3
print("even number= ",num)
print("odd number= ",num1)
print("sum of even number=",sum)
print("sum of odd number=",sum1)
print("count even :",count1)
print("count odd :",count2)
print("average of even no.",average)
print("average of odd no.",average1)
print("average of all no.",average3)
print("total count",count3)
print("sum of all no.",sum3)

# 💔even number=[14,56,12,43]
# 🤎odd number=[23,19, 9, 15, 25, 31,43]
# 🖤 Sun of even number=124
# ❤️ Sum of odd number= 165
# 💜 Count even:4
# 💙Count odd : 7
# 💗 average of even no.31.0
# 💓 average of odd no. 23.571...
# 💞 total of all no. 26.272...
# 💖 Sum of all no. 289