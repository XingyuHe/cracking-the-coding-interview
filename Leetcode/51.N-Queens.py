class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.all_result = []
        track = []
        self.place_c( n, 0, track)

        return self.creat_solutions(n)

    def creat_solutions(self, n):

        solutions = [[["." for _ in range(n)] for _ in range(n)] for _ in range(len(self.all_result))]
        print len(self.all_result), len(self.all_result[0])

        for i in range(len(self.all_result)):

            board_positions = self.all_result[i]

            for coordinate in board_positions:
                print len(coordinate)
                r = coordinate[0]
                c = coordinate[1]
                solutions[i][r][c] = "Q"
            for j in range(len(solutions[i])):
                solutions[i][j] = "".join(solutions[i][j])

        return solutions

    def place_c(self, n, c, track):
        if c == n:
            self.all_result.append(track[:])

        for r in range(n):
            if self.check(track, r, c):

                track.append([r, c])
                self.place_c( n, c + 1, track)
        if c > 0:
            track.pop()
        else:
            return

    def check(self, track, r, c):

        for coordinate in track:
            if r == coordinate[0]:
                return False
            if c == coordinate[1]:
                return False
            if abs(coordinate[0] - r) == abs(coordinate[1] - c):
                return False
        return True

solution = Solution()
print solution.solveNQueens(4)