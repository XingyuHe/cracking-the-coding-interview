# O(MxN)
import unittest


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = matrix
    zero_i = {}
    zero_j = {}

    for i in range(m):
        for j in range(n):
            if new_matrix[i][j] == 0:
                zero_i[i] = 1
                zero_j[j] = 1

    for i in zero_i.keys():
        for j in range(n):
            new_matrix[i][j] = 0

    for j in zero_j.keys():
        for i in range(m):
            new_matrix[i][j] = 0

    return new_matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
