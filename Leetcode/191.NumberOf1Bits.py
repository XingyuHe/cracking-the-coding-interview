def hammingWeight(n):
	
	if n == 0:
		return 0
	div, rem = divmod(n, 2)
	return hammingWeight(div) + rem

print hammingWeight(11)
	
	
	
