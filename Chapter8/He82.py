class Solution(object):

    def __init__(self):
        self.path = []


    def visit(self, maze, x, y):

        if x == len(maze) or y == len(maze[0]):
            return False
        if maze[x][y]:

            if x == len(maze) - 1 and y == len(maze[0]) - 1:
                self.path.append([x, y])
                return True

            for i, j in zip([1,0],[0,1]):
                new_x = x + i
                new_y = y + j

                result = self.visit(maze, new_x, new_y)
                if result:
                    self.path.append([x, y])
                    return True


solution = Solution()
solution.visit([[True, False],[True,False]], 0, 0)
print(solution.path)