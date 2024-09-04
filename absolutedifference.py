arr=[12,3,14,5,6,77,13]
num=13
diff=2
count=0
for i in arr:
    a=(abs(num-i))
    if a <= diff:
        count+=1
print(count)