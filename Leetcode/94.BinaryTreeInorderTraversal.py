def inOrderTraversal(root):

    if not root:
        return []
    left = inOrderTraversal(root.left)
    left.append(self.val)
    left.extend(inOrderTraversal(root.right))
    return left


def stackSolution(root):

    stk = [root]
    ans = []

    while stk:

        last_node = stk[-1]

        if last_node:
            if not last_node.left:
                ans.append(last_node.val)

                stk.pop()
                stk.append(last_node.right)
            else:
                stk.append(last_node.left)

        else:
            stk.pop()


