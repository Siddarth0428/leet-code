from heapq import heappush, heappop

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        left, right = 0, len(costs) - 1

        for _ in range(candidates):
            if left <= right:
                heappush(left_heap, (costs[left], left))
                left += 1

        for _ in range(candidates):
            if left <= right:
                heappush(right_heap, (costs[right], right))
                right -= 1

        total = 0

        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                _, index = heappop(left_heap)
                total += costs[index]
                if left <= right:
                    heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                _, index = heappop(right_heap)
                total += costs[index]
                if left <= right:
                    heappush(right_heap, (costs[right], right))
                    right -= 1

        return total