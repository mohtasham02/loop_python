a=int(input('enter number'))
rev=0
x=a
while a>0:
	rev=(rev*10)+a%10
	a=a//10
a+=1
if x==rev:
	print('palindrome number',rev)
else:
	print('not a palindrome number',rev)
    