def isPalindrome(s):
    import string

    ignore_set = set(string.punctuation)
    ignore_set.add(" ")
    s_lower = s.lower()
    reverse_i = len(s) - 1
    i = 0
    while reverse_i >= 0 and i < len(s_lower):

        if reverse_i <= i:
            return True

        front_char = s_lower[i]
        back_char = s_lower[reverse_i]

        if front_char in ignore_set:
            i += 1
        elif back_char in ignore_set:
            reverse_i -= 1
        else:
            if back_char != front_char:
                return False
            i += 1
            reverse_i -= 1

    return True

def Faster1(s):
    s = [x.lower() for x in s if x.isalnum]
    return s == s[::-1]

def Faster(s):
    s = filter(str.isalnum, s).lower()
    return s == s[::-1]
print isPalindrome("aba")
print Faster("abcdefgd")
print Faster1("abcef")
print isPalindrome("")
print isPalindrome(" ")

