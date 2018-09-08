from LinkedList import LinkedList


def remove_dups(ll):
    if ll.head == None:
        return
    current = ll.head
    runner = current.next

    record = set([current.value])
    while runner != None:

        if runner.value in record:
            runner = runner.next
            current.next = runner

        else:
            record.add(current.value)
            current = runner
            runner = runner.next

def remove_dups_followup(ll):
    current = ll.head


    while current != None:

        runner = current

        while runner.next != None:

            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next


ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
print()
remove_dups(ll)
print(ll)

print()
ll.generate(100, 0, 9)
print(ll)
print()
remove_dups_followup(ll)
print(ll)
