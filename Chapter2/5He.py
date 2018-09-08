from LinkedList import LinkedList


def sum_lists(ll_a, ll_b):

    ll = LinkedList()
    curr_a = ll_a.head
    curr_b = ll_b.head
    carry = 0

    while curr_a or curr_b:
        result = carry
        if curr_a:
            result += curr_a.value
            curr_a = curr_a.next

        if curr_b:
            result += curr_b.value
            curr_b = curr_b.next

        carry = result // 10
        ll.add(result % 10)

    if carry:
        ll.add(carry)

    return ll


def sum_lists_followup(ll_a, ll_b):

    ll = LinkedList()

    if len(ll_a) > len(ll_b):
        for _ in range(len(ll_a) - len(ll_b)):
            ll_b.add_to_beginning(0)
    else:
        for _ in range(len(ll_b) - len(ll_a)):
            ll_a.add_to_beginning(0)
    na = ll_a.head
    nb = ll_b.head
    result = 0

    print(ll_b)
    print(ll_a)
    while na and nb:

        multiply = na.value + nb.value
        carry = multiply // 10
        ll.add(result + carry)
        print(result, "result")
        print(carry, "carry")
        result = multiply % 10

        na = na.next
        nb = nb.next
    ll.add(result)



    return ll


ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print()
print(sum_lists(ll_a, ll_b))
print()
print(sum_lists_followup(ll_a, ll_b))
