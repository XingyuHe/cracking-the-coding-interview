import copy
def permute(orig_list):

    if len(orig_list) == 1:
        return [[orig_list[0]]]

    permutations = permute(orig_list[1:])
    new_permutation = []

    for permutation in permutations:

        for i in range(len(permutation) + 1):
            temp = copy.deepcopy(permutation)
            temp.insert(i, orig_list[0])

            new_permutation.append(temp)

    return new_permutation


a = list("abcdefg")
permutation = permute()
stringPerm = []
for i in permutation:
    stringPerm.append("".join(i))
print stringPerm
print len(permute(a))