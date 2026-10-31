class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # resolve(r, c, direction) returns the empty cell reached,
        # or None if the reflection chain exits the grid.
        # direction: 0 = entering while moving right, 1 = moving down
        memo = {}

        def resolve(r: int, c: int, direction: int):
            if not (0 <= r < m and 0 <= c < n):
                return None
            if grid[r][c] == 0:
                return (r, c)

            key = (r, c, direction)
            if key not in memo:
                if direction == 0:  # entered moving right; reflect down
                    memo[key] = resolve(r + 1, c, 1)
                else:               # entered moving down; reflect right
                    memo[key] = resolve(r, c + 1, 0)

            return memo[key]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # Every resolved move goes down, right, or both, so row-major
        # order processes each destination after its possible sources.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 or dp[r][c] == 0:
                    continue

                for nr, nc, direction in (
                    (r, c + 1, 0),  # try right
                    (r + 1, c, 1),  # try down
                ):
                    dest = resolve(nr, nc, direction)
                    if dest is not None:
                        dr, dc = dest
                        dp[dr][dc] = (dp[dr][dc] + dp[r][c]) % MOD

        return dp[m - 1][n - 1]