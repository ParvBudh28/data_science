is_prime=[True]*100005
primes=list()

# MakeSieve function to get all prime factors till 10^5
def makeSieve():
	is_prime[0]=is_prime[1]=False
	
	for i in range(4,100005,2):
		is_prime[i]=False

	primes.append(2)

	# for all the numbers greater than 3
	for i in range(3,100005,2):
		if is_prime[i]:
			primes.append(i)
			for j in range(i**2,100005,i):
				is_prime[j]=False

	return


# solve function that prints all the prime numbers in range a,b
def solve():
	# Input
	a,b=input().split()
	a=int(a)
	b=int(b)

	size=b-a+1
	isPrime=[True]*size

	if a==1:
		isPrime[0]=False

	for i in primes:

		if i*i>b:
			break

		start=a+i-1
		start=start//i
		start*=i

		for j in range(max(i*i,start),b+1,i):
			isPrime[j-a]=False

	for i in range(a,b+1):
		if isPrime[i-a]:
			print(i,end=" ")

	print()


# call the makeSieve() function to initialise primes
makeSieve()

# t represents the number of testcases
t=int(input())



for _ in range(t):
	solve()


