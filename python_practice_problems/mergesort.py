def merge(a,start,end):
	
	# print(f"start:{start}, end:{end}")

	mid=(start+end)//2
	i,j=start,mid+1

	temp=list()

	while i<=mid and j<=end:
		if a[i]<=a[j]:
			temp.append(a[i])
			i+=1
		else:
			temp.append(a[j])
			j+=1

	while i<=mid:
		temp.append(a[i])
		i+=1
	while j<=end:
		temp.append(a[j])
		j+=1

	# print(f"len of temp is {len(temp)}")

	for index in range(len(temp)):
		# print(start+index)
		a[start+index]=temp[index]

	return

def mergesort(a,start,end):
	if start>=end:
		return

	mid=(start+end)//2
	mergesort(a,start,mid)
	mergesort(a,mid+1,end)

	merge(a,start,end)
	return


n=int(input())
el=input()
el=el.split()
a=[int(x) for x in el]

mergesort(a,0,n-1)
for i in range(len(a)):
	print(a[i],end=' ')
