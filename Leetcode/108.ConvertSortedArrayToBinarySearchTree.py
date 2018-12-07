class  TreeNode(object):

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):

    def helper(nums, left_i, right_i):
        print left_i, right_i

        if not nums or right_i < left_i:
            print "None"
            return None

        curr_val_i = (right_i + left_i) // 2
        left_node = helper(nums, left_i, curr_val_i - 1)
        right_node = helper(nums, curr_val_i + 1, right_i)
        current_node = TreeNode(nums[curr_val_i])
        current_node.left = left_node
        current_node.right = right_node

        return current_node


    return helper(nums, 0, len(nums) - 1)

def Faster(nums):

    if not nums:
        return None

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = self.Faster(nums[:mid])
    node.right = self.Faser(nums[mid + 1:])

    return node

sortedArrayToBST([1,2,3,4,5,6])


