from LinkedList import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    if fast:
        slow = slow.next
    print(stack)
    while slow:
        if slow.value != stack.pop():
            return False

        slow = slow.next

    return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
