def isPalindrome(head):

    # Space is O(n)
    if not head or not head.next:
        return True

    curr = runner = head
    stk = []

    while runner.next:

        stk.append(curr.val)
        curr = curr.next
        runner = runner.next.next

    if runner:
        curr = curr.next

    while curr:
        if curr.val != stk.pop():
            return False

        curr = curr.next

    return True

def Faster(head):


