from LinkedList import LinkedList


def kth_to_last(ll, k):
    curr = runner = ll.head

    index = 0
    while runner:
        runner = runner.next
        index += 1
        if index == k - 1:
            break

    while runner.next:
        curr = curr.next
        runner = runner.next

    return curr.value

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
