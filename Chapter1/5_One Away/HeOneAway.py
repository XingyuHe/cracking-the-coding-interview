# O(N)
import unittest


def one_away(s1, s2):
    diff_len = len(s1) - len(s2)

    if diff_len > 1 or diff_len < -1:
        return False

    if diff_len != 0:
        shortstring, longstring = (s2, s1) if diff_len > 0 else (s1, s2)
        short_len = len(shortstring)
        short_index = long_index = 0
        while short_index < short_len:
            if shortstring[short_index] != longstring[long_index]:
                long_index += 1
                while short_index < short_len:
                    if shortstring[short_index] != longstring[long_index]:
                        return False
                    short_index += 1
                    long_index += 1
            short_index += 1
            long_index += 1
        return True

    if diff_len == 0:
        index = 0
        while index < len(s1):
            if s1[index] != s2[index]:
                index += 1
                while index < len(s1):
                    if s1[index] != s2[index]:
                        return False
                    index += 1
            index += 1
        return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
