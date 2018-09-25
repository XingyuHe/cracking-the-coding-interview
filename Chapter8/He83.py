def MagicIndex(array, min, max):

    magic_indices = []
    i = 0
    while True:
        if i >= len(array):
            break
        curr_num = array[i]

        if curr_num > i:
            i = curr_num
        elif curr_num == i:
            magic_indices.append(i)
            i += 1
        else:
            i += 1

    return magic_indices




def FillArray():
    array = [0] * 10
    array[0] = -14
    array[1] = -12
    array[2] = 0
    array[3] = 1
    array[4] = 2
    array[5] = 5
    array[6] = 9
    array[7] = 10
    array[8] = 23
    array[9] = 25
    return array

array = FillArray()
print MagicIndex(array, 0, len(array) - 1)
