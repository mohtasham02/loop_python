num=int(input("enter number"))
orig=num
a=1
c=0
while a<=num:
    if num%a==0:
        c+=1
    a+=1
if c==2:
    print("prime number",orig)
else:
    print("not a prime number",orig)
