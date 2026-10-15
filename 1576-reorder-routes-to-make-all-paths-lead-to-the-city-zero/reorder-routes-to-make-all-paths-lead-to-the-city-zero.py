from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))  # a -> b points away when traversed from a
            graph[b].append((a, 0))  # b -> a already points toward a

        changes = 0
        stack = [(0, -1)]

        while stack:
            city, parent = stack.pop()

            for neighbor, needs_reversal in graph[city]:
                if neighbor == parent:
                    continue
                changes += needs_reversal
                stack.append((neighbor, city))

        return changes
        