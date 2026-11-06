class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted(enumerate(queries), key=lambda item: item[1])

        counts = [0] * (n + 1)
        active_servers = 0
        left = right = 0
        result = [0] * len(queries)

        for index, q in ordered_queries:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if counts[server] == 0:
                    active_servers += 1
                counts[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active_servers -= 1
                left += 1

            result[index] = n - active_servers

        return result