n=int(input())

arr=list()
for i in range(n):
	x=int(input())
	arr.append(x)

ans=True
dec=True


for i in range(n-1):
	if arr[i]==arr[i+1]:
		ans=False
		break
	if arr[i]<arr[i+1] and dec:
		dec=False
	if not dec and arr[i]>arr[i+1]:
		ans=False
		break

if ans:
	print("true")
else:
	print("false")
