import math
t=int(input())

def solve():
    n=int(input())
    for a in range(int(math.sqrt(n))+1):
        rem=n-a*a
        if rem<0:
        	break
        b=math.sqrt(rem)
        if b==int(b) and a<=b:
            print(f"({a},{int(b)})",end=' ')

for _ in range(t):
    solve()
    print()