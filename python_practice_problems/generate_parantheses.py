n = int(input())

def solve(left,right,n,curr):

	if right>left:
		return

	if left+right==2*n and left!=right:
		return
	
	if left+right==2*n and left==right:
		for i in curr:
			print(i,end="")
		print()
		return
	
	if left>right:
		curr.append(')')
		solve(left,right+1,n,curr)
		curr.pop()

	curr.append('(')
	solve(left+1,right,n,curr)
	curr.pop()
	return


solve(0,0,n,[])