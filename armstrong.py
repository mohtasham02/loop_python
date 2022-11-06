i=int(input("enter number"))
sum=0
orig=i
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("armstrong number")
else:
    print("not a armstrong number")
