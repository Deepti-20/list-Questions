magic=[[8,3,4],[1,5,9],[6,7,2]]
sum=magic[0][0]+magic[1][0]+magic[2][0]
sum1=magic[0][0]+magic[1][1]+magic[2][2]
sum2=magic[0][2]+magic[1][1]+magic[2][0]
if sum==sum1==sum2:
	print("it is magic square")
else:
	print("it is not a magic square")

# 💔 Magic square without using loop 💔