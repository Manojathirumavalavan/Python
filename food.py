a = "Food is essential for life, providing the necessary nutrients and energy."
c=0
for i in range(len(a)):
    if(a[i]==' ' and a[i+1]!=' '):
       c=c+1 
print("The num of words: ",c+1)