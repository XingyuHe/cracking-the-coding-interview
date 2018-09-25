sun = [0]
units = [0.25, 0.1, 0.05, 0.01]

def change(n):

    change_helper(n, 0)

def change_helper(n, unit_index):

    if n == 0:
        sun[0] += 1

    if n < 0:
        return

    if unit_index == 4:
        return
    tempn = n
    unit = units[unit_index]


    max_unit = tempn // unit

    for i in range(int(max_unit + 1)):
        remaining = tempn - i * unit
        change_helper(remaining, unit_index + 1)


change(0.25)
print sun