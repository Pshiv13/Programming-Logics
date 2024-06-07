""" You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4 """


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        num_min = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        if num_fresh == 0:
            return 0

        while q:
            l = len(q)
            num_min += 1
            for _ in range(l):
                r, c = q.popleft()
                for r, c in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        q.append((r, c))
                        num_fresh -= 1

        if num_fresh == 0:
            return num_min - 1
        else:
            return -1
