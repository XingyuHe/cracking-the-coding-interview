# O(N)
import unittest


def unique(string):
    if len(string) > 256:
        return False

    counted_list = [False for i in range(256)]
    for char in string:
        value = ord(char)

        if counted_list[value]:
            return False

        counted_list[value] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abc¬˚ød'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
