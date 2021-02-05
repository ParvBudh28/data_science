import random

def quicksort(a,start,end):
	if start>=end:
		return
	i=start-1
	for j in range(start,end):
		if a[j]<a[end]:
			i+=1
			a[i],a[j]=a[j],a[i]
	i+=1
	a[i],a[end]=a[end],a[i]
	quicksort(a,start,i-1)
	quicksort(a,i+1,end)
	return

n=int(input())
a=[int(x) for x in input().split()]

random.shuffle(a)
quicksort(a,0,n-1)

for i in a:
	print(i,end=' ')
