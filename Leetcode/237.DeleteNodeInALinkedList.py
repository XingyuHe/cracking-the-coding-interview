def deleteNode(node):

    next_node = node.next

    node.val = next_node.val
    node.next = next_node.next
    next_node = None


