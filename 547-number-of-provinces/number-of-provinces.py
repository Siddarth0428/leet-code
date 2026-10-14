class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city in visited:
                continue

            provinces += 1
            stack = [city]
            visited.add(city)

            while stack:
                current = stack.pop()
                for neighbor in range(n):
                    if isConnected[current][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        return provinces