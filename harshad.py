num=int(input('enter number'))
rem=sum=0
temp=num
while temp>0:
	rem=temp%10
	sum=sum+rem
	temp=temp//10
if num%sum==0:
	print('harshad number',num)
else:
	print('not harshad number',num)