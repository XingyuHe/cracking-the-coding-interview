def getIntersectionNode(head1, head2):
    n1, n2 = headA, headB


    r1 = set([])
    r2 = set([])
    while n1 or n2:
        if n1:
            r1.add(n1)
        if n2:
            r2.add(n2)

        if n1 in r2:
            return n1

        if n2 in r1:
            return n2

        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

    return None

def Faster(headA, headB):

    lenA = lenB = 0
    na, nb = headA, headB

    while na:

        na = na.next
        lenA += 1
    while nb:

        nb = nb.next
        lenB += 1

    na, nb = headA, headB

    if lenA > lenB:

        for _ in range(lenA - lenB):

            na = na.next
    elif lenA < lenB:

        for _ in range(lenB - lenA):

            nb = nb.next

    while na != nb:

        na = na.next
        nb = nb.next

    return na

