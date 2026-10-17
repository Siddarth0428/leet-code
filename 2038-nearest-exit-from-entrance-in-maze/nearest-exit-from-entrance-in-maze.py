from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance
        queue = deque([(start_r, start_c, 0)])
        maze[start_r][start_c] = "+"  # mark visited

        while queue:
            r, c, steps = queue.popleft()

            if (r, c) != (start_r, start_c) and (
                r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            ):
                return steps

            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    maze[nr][nc] = "+"  # mark visited when enqueued
                    queue.append((nr, nc, steps + 1))

        return -1