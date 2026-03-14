name=['Gill','Abi','Ken','Varun']
age=[23,45,65,33]
loc=['Chennai','Trichy','Salem','Pondy']

res=list(zip(age,name,loc))
res1=sorted(res)
for i in range(4):
    print("{}.{} age i {} lives in {}".format(i+1,res1[i][1],res1[i][0],res1[i][2]))
    