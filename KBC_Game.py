# print("Aapka question hai :")
# question_list = [
#     "How many continents are there?",              # pehla question
#     "What is the capital of India?",            # doosra question
#     "NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]
# options_list = [
#     #pehle question ke liye options
#     ["Four", "Nine", "Seven", "Eight"],
#     #second question ke liye options
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     #third question ke liye options
#     ["Software Engineering", "Counseling",".Tourism", "Agriculture"]]
# i=0
# solution_list=[3,4,1]
# while i<len(options_list):
# 	print('Q.',i+1,question_list[i])
# 	j=0
# 	print("Aapke options hai :-")
# 	while j<len(options_list[i]):
# 		print(j+1,options_list[i][j])
# 		j=j+1
# 	user=int(input("enter any number"))
# 	if user==solution_list[i]:
# 		print("congrats your ans is correct")
# 	else:
# 		print("your ans is wrong")
# 		break
# 	i=i+1
# 	print()

# # KBC: final code:-
# # 😌 Question pucha and options diye uske baad jo user ne input diya  check 
# # kiya ki user ka ans sahi hai ya galat. 
# # Agar ans galat hai to user ko out krna tha.😌



question_list=["How many continents are there ?","What is the capital of India ?",
"NG mei kaun se course padhaya jaata hai ? "]

options_list=[["Four","Nine","Seven","Eight"],
["Chandigarh","Bhopal","Chennai","Delhi"],
["Software Engineering","Counseling","Tourism",
"Agriculture"]]
life_line=[["Seven","Eight"],["Bhopal","Delhi"],["Software Engineering","Counseling"]]
solution_list2=[1,2,1]
i=0
count=0
solution_list=[3,4,1]
while i<len(question_list[i]):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	user=int(input("enter any no. "))
	if user==solution_list[i]:
		print("congrates your ans is correct")
	elif user==5050:
		if count==0:
			k=0
			while k<len(life_line[i]):
				print(k+1,life_line[i][k])
				k=k+1
			count=count+1
			user2=int(input("enter any no. "))
			if user2==solution_list2[i]:
				print("you are right")
			else:
				print("wrong ans. :")
		else:
			print("aapne life line use kr li hai")
			num=int(input("enter any no. "))
			if num==solution_list[i]:
				print("right answer")
			else:
				print("wrong answer")
				break
	else:
		print("galat jawab")
		break
	i=i+1
		