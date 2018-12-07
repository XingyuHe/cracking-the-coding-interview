def romanToInt(s):

    sd = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}

    number_list = []

    for symbol in s:

        number_list.append(sd[symbol])

    prev_num = number_list[0]
    summ = 0

    for n in number_list:

        summ += n

        if n > prev_num:

            summ -= 2 * prev_num

        prev_num = n

    return summ

def Faster(s):

    for i in range(len(s)):

        if i > 0 and d[s[i]] > d[s[i - 1]]:

            res += d[s[i]] - 2 * d[s[i -  1]]
        else:

            res += d[s[i]]

    return res

print romanToInt("IX")

