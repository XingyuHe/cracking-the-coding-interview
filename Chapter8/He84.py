import copy
perm_list = []
orig_list = [1, 2, 3, 4]

def all_subset(n = 0, power_set = []):
    print n
    additional_subset = []
    if n == len(orig_list):
        return power_set

    if n == 0:
        power_set.append([])

    for subset in power_set:
        newsubset = copy.deepcopy(subset)
        newsubset.append(orig_list[n])
        additional_subset.append(newsubset)

    power_set.extend(additional_subset)
    return all_subset(n + 1, power_set)


def combinatorics():

    n = len(orig_list)
    max_num = 1 << n
    power_set = []

    for i in range(max_num):

        j = copy.deepcopy(i)
        temp_set = []
        index = 0
        while j > 0:
            if j & 1 == 1:
                temp_set.append(orig_list[index])

            index += 1
            j = j >> 1
        power_set.append(temp_set)

    return power_set


print combinatorics()
print len(perm_list)