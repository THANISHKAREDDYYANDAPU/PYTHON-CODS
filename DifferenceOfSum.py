a=6
b=30
sum=0
add=0
for i in range(1,a+1):
    if i%b == 0:
        sum += i
    else:
        add += i
print(add-sum)