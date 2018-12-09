class ListNode(object):

    def __init__(x):

        self.val = 0
        self.next = None

def hasCycle(head):
    if not head:
        return False
    fq = set([])

    node = head
    
    while node:
        if node in fq:
            return True

        fq.add(node)
        node = node.next

    return False

def Smaller(head):

    if not head:
        return False

    curr = runner = head

    while runner and runner.next:
        runner = runner.next.next

        curr = curr.next
        if curr == runner:
            return True

    return False
