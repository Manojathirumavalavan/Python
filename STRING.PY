a=input("Enter any string: ")
result = ""
count = 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
    else:
        result += a[i] + str(count)
        count = 1
result += a[-1] + str(count)

print(result)