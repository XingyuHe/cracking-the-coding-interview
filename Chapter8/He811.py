sun = [0]
result = []
units = [25, 10, 5, 1]

def change(n):

    change_helper(n, 0)

def change_helper(n, unit_index, history=()):

    if n == 0:
        print "found one", history
        sun[0] += 1
        result.append(history)

    elif n < 0:
        pass

    elif unit_index == 4:
        pass

    else:

        unit = units[unit_index]


        max_unit = n // unit

        print unit, max_unit, n
        for i in range(int(max_unit + 1)):

            remaining = n - i * unit
            print unit, i, remaining, max_unit
            change_helper(remaining, unit_index + 1, history + (i, unit))
        print "end loop"

cache = {}
def change2(n):


    return change2_helper(n, 0)

def change2_helper(n, unit_index):

    if unit_index == 3:
        return 1, [1] * n
    if (n, unit_index) in cache:
        return cache[(n, unit_index)]

    ways = 0
    history = []
    unit = units[unit_index]
    max_unit = n // unit
    for i in range(int(max_unit + 1)):

        remaining = n - i * unit
        subways, subhistory = change2_helper(remaining, unit_index + 1)
        ways += subways
        history.extend(subhistory)

    cache[(n, unit_index)] = [ways, history]
    return ways, history



change(25)
print change2(25)