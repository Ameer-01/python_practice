n=int(input())
temp=n
o=len(str(n))
sum=0
##for i in str(n):
##    sum=sum+(int(i)**o)
while n!=0:
    r=n%10
    sum=sum+(r**o)
    n=n//10
if sum==temp:
    print("yes")
else:
    print("no")
        
        
