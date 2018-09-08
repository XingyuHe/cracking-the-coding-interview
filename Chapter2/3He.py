from LinkedList import LinkedList


def delete_middle_node(node, ll):
    curr = ll.head
    while curr:
        if curr.next is node:
            curr.next = curr.next.next
            break
        curr = curr.next



ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node, ll)
print(ll)
