def mergeTwoLists(L1, L2):

    n1, n2 = L1, L2
    while n1 and n2:

        if n1.val >= n2.val:
            insert_val = delete(n2)
            next1 = n1.next
            n1.next = ListNode(insert_val)
            n1.next.next = next1
            
        n1 = n1.next
        n2 = n2.next        


def delete(node):
    
    if not node.next:
        return node

    return_val = node.val
    node.val = node.next.val
    node.next = node.next.next   
    

    return return_val

def return_new_list(l1, l2):
    # It turns out a better way to do this is 
    if l1 or l2:
        return l1 or l2
    # My original ways
    if not l1:
        return l2
    if not l2:
        return l1
    new = ListNode(10)
    head = new
    n1, n2 = l1, l2
    while n1 and n2:
        if n1.val < n2.val:
            new.next = ListNode(n1.val)
            n1 = n1.next

        else:
            new.next = ListNode(n2.val)
            n2 = n2.next

        new = new.next
    # A better way to do this is 
    new.next = n1 or n2
    # My original way 
    if n1:
        new.next = n1
    if n2:
        new.next = n2
    return head.next
        
