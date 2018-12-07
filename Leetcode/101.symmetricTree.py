def isSymmetric(root):
	if not root:
		return True

	stack_r = [root.right]
	stack_l = [root.left]
	while stack_r and stack_l:

		right = stack_r.pop()
		left = stack_l.pop()

		if (not right and left) or (not left and right):
			return False
		elif right and left: 
			if right.val != left.val:
				return False
			else:
				stack_r.append(right.left)
				stack_r.append(right.right)
				stack_l.append(left.right)
				stack_l.append(left.left)
					

	return True
