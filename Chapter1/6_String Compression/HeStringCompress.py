# O(N)
import unittest


def string_compression(string):
    new = ""
    current_index = 0

    while current_index < len(string):

        char = string[current_index]
        runner = current_index + 1

        while runner < len(string) and string[runner] == char:
            runner += 1

        new += char + str(runner - current_index)
        current_index = runner

    if len(new) < len(string):
        return new
    return string

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
