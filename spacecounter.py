string=input("enter your msg=")
c=0
for i in string:
	if(i.isspace()):
		c+=1
print("Number of Spaces : "+str(c))
