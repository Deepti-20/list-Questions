string="the quick brown fox jumped over the lazy  dog. the dog slept over the verandah."
sub=string.split()
i=0
a=' '
while i<len(sub):
	if sub[i]=="over":
		pass
	else:
		a=a+sub[i]
	i=i+1
print(a)