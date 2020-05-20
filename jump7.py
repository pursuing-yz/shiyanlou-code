x=1
while x<=100:
	if x%7==0 or x/10==7 or x%10==7:
		x+=1
		continue
	print(x)
	x+=1