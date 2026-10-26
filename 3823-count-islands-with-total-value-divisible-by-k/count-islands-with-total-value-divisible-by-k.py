from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total = 0
                stack = [(r, c)]
                total += grid[r][c]
                grid[r][c] = 0  # mark visited

                while stack:
                    row, col = stack.pop()

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                            total += grid[nr][nc]
                            grid[nr][nc] = 0  # mark visited
                            stack.append((nr, nc))

                if total % k == 0:
                    islands += 1

        return islands