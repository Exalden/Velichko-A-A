# -- coding: utf-8 --
def D():
	sum=0
	n=int(input())
	a=0
	b=1
	for i in range(2,n+1):
		sum+=b
		c=b
		b+=a
		a=c
		
	return sum
print(D())