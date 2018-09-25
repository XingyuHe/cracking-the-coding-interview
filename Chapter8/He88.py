import copy
def duplicate_permute(string):
    freq_dict = {}
    for i in string:
        if i in freq_dict:
            freq_dict[i] += 1

        else:
            freq_dict[i] = 1

    return duplicate_mutate_helper1(len(string), "", freq_dict)

def duplicate_mutate_helper1(remaining, prefix, freq_dict):

    print prefix, remaining, freq_dict

    if remaining == 0:
        result.append(prefix)

    keys = freq_dict.keys()


    for key in keys:
        count = freq_dict[key]
        print "loop another", key
        if count > 0:
            freq_dict[key] -= 1
            duplicate_mutate_helper1(remaining - 1, prefix + key, freq_dict)
            freq_dict[key] = count

result = []
def duplicate_permute2(string):
    freq_dict = {}
    for i in string:
        if i in freq_dict:
            freq_dict[i] += 1

        else:
            freq_dict[i] = 1

    return duplicate_mutate_helper2(len(string), (), freq_dict)

def duplicate_mutate_helper2(remaining, prefix, freq_dict):

    print prefix, remaining, freq_dict

    if remaining == 0:
        result.append(prefix)

    keys = freq_dict.keys()


    for key in keys:
        count = freq_dict[key]
        print "loop another", key
        if count > 0:
            freq_dict[key] -= 1
            local_prefix = prefix + (key, )
            duplicate_mutate_helper2(remaining - 1, local_prefix, freq_dict)
            freq_dict[key] = count
    print result, len(result)

print duplicate_permute2(list("1234"))

print(result)