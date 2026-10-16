from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def divide(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                current, product = queue.popleft()

                for neighbor, weight in graph[current]:
                    if neighbor in visited:
                        continue

                    next_product = product * weight
                    if neighbor == end:
                        return next_product

                    visited.add(neighbor)
                    queue.append((neighbor, next_product))

            return -1.0

        return [divide(a, b) for a, b in queries]
        