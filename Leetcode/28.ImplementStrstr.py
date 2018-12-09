def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):

        j = 0
        while j < len(needle) and needle[j] == haystack[i + j]:
            j += 1

        print j
        if j == len(needle):
            return i

    return -1

print strStr("happy", 'pp')
print strStr("", "")

