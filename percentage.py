name=['GILL','ABI','RAHUL','JOHN','ANU']
marks=[[30,40,50],[67,88,90],[90,76,72],[90,76,67],[43,32,21]]

for i in range(5):
    total = sum(marks[i])
    percentage = total / 3
    
    if percentage >=90:
        grade="S"
    elif percentage >=60:
        grade="A"
    elif percentage >=40:
        grade="B"
    else :
        grade="Fail"
        
    print("{} scored {}% and Grade is {}".format (name[i],percentage,grade))