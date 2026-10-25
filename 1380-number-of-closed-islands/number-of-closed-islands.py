class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flood(r: int, c: int) -> bool:
            # Mark visited so this land cell is not counted again.
            grid[r][c] = 1
            is_closed = r not in (0, rows - 1) and c not in (0, cols - 1)

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if not flood(nr, nc):
                        is_closed = False

            return is_closed

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and flood(r, c):
                    count += 1

        return count