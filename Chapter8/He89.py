result = []
paren_dict = {"(":1,
              ")":-1}

def permute_parenthesis(n):

    freq_dict = {}
    freq_dict["("] = n
    freq_dict[")"] = n
    permute_parenthesis_helper( 0, n*2, "", freq_dict)


def permute_parenthesis_helper( summ, remaining, cache, freq_dict):

    if remaining == 0:
        result.append(cache)

    paren_choice = ["(", ")"] if summ > 0 else ["("]

    for paren in paren_choice:

        count = freq_dict[paren]
        if count > 0:

            value = paren_dict[paren]

            freq_dict[paren] -= 1

            permute_parenthesis_helper(summ + value, remaining - 1, cache + paren, freq_dict)

            freq_dict[paren] = count

permute_parenthesis(1)
print result