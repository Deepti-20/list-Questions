# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest

list1=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
string=""
i=0
while i<len(list1):
    j=0
    while j<len(list1[i]):
        string=list1[i][j]
        print(string,end="")
        j=j+1
    i=i+1
