def longestUnivaluePath(root):

    self.mx = 0
    self.helper(root)
    return self.mx


def helper(self, root):

    if not root:
        return 0, "a"
    left_score, left_number = self.helper(root.left)
    right_score, right_number = self.helper(root.right)
    left_score = left_score if left_number == root.val else 0
    right_score = right_score if right_number == root.val else 0

    root_score = max(left_score, right_score) + 1
    self.mx = max(self.mx, root_score)
    return max(right_score, left_score), self.val
