# O(N)
import unittest


def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    lower = phrase.lower()
    count = [0 for _ in range(128)]
    count_odd = 0

    for i in lower:
        if i != " ":

            value = ord(i)
            count[value] += 1

            count_odd += 1 if count[value] % 2 else -1

    return count_odd < 2

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
