#perfect number
num=int(input("enter number"))
sum=0
i=1
while i<=num//2:
    if num%i==0:
        sum+=i
    i+=1
if sum==num:
    print("prefect")
else:
    print("not perfect")
