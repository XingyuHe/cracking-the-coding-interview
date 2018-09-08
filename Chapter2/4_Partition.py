from LinkedList import LinkedList


def partition(ll, x):

    first = ll.head
    final = ll.tail

    curr = first

    while curr.next.next:
        curr = curr.next

    print(curr.value, final.value)
    print('==', curr.next == final)
    print('is', curr.next is final)


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)
