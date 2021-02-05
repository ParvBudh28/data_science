n=int(input())

for i in range(n):
	for j in range(n-i):
		print(j+1,end=' ')

	if i>0:
		for j in range(2*i-1):
			print('*',end=' ')
	print()

