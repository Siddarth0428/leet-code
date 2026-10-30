import heapq


class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))

        # dist[node][run] is the shortest distance reaching node with
        # a trailing run of `run` identical labels.
        inf = float("inf")
        dist = [[inf] * (k + 1) for _ in range(n)]
        start_run = 1
        dist[0][start_run] = 0
        heap = [(0, 0, start_run)]

        while heap:
            cost, node, run = heapq.heappop(heap)

            if cost != dist[node][run]:
                continue
            if node == n - 1:
                return cost

            for neighbor, weight in graph[node]:
                if labels[neighbor] == labels[node]:
                    if run == k:
                        continue
                    next_run = run + 1
                else:
                    next_run = 1

                next_cost = cost + weight
                if next_cost < dist[neighbor][next_run]:
                    dist[neighbor][next_run] = next_cost
                    heapq.heappush(heap, (next_cost, neighbor, next_run))

        return -1