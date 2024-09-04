str="abc.bc.bcd.bcd"
count=0

#count1=0
for i in str:
    if i>='a' and i<='z':
        count+=1
    if i=='.':
        count=0
print(count)
        