n=int(input())
sum=0

for i in range(1,n+1):
    digit=0
    num=i
    while(num>0):
        digit+=1
        num=num//10
    if digit%2!=0:
       sum+=1
print(sum)
    

    
    