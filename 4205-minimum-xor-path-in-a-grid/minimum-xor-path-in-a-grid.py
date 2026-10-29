from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        dp = [set() for _ in range(cols)]

        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if r == 0 and c == 0:
                    reachable = {0}
                else:
                    reachable = set()
                    if r > 0:
                        reachable.update(dp[c])
                    if c > 0:
                        reachable.update(dp[c - 1])

                dp[c] = {x ^ value for x in reachable}

        return min(dp[-1])