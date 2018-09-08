from LinkedList import LinkedList


def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False


    curra, currb = list1.head, list2.head
    if len(list1) > len(list2):
        for _ in range(len(list1) - len(list2)):
            curra = curra.next
    else:
        for _ in range(len(list1) - len(list2)):
            curra = curra.next

    while curra is not currb:

        curra = curra.next
        currb = currb.next

    return curra