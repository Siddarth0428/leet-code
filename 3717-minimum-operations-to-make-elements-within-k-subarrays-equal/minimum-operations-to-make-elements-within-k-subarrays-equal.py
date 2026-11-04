from typing import List


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        return total

    def kth(self, k: int) -> int:
        """Return the smallest index i whose prefix sum is at least k."""
        i = 0
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = i + step
            if nxt <= self.n and self.tree[nxt] < k:
                i = nxt
                k -= self.tree[nxt]
            step >>= 1
        return i + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        values = sorted(set(nums))
        rank = {value: i + 1 for i, value in enumerate(values)}

        counts = Fenwick(len(values))
        sums = Fenwick(len(values))
        window_sum = 0
        costs = []

        for i, value in enumerate(nums):
            idx = rank[value]
            counts.add(idx, 1)
            sums.add(idx, value)
            window_sum += value

            if i >= x:
                old = nums[i - x]
                old_idx = rank[old]
                counts.add(old_idx, -1)
                sums.add(old_idx, -old)
                window_sum -= old

            if i >= x - 1:
                median_idx = counts.kth((x + 1) // 2)
                median = values[median_idx - 1]

                left_count = counts.prefix_sum(median_idx)
                left_sum = sums.prefix_sum(median_idx)
                right_count = x - left_count
                right_sum = window_sum - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )
                costs.append(cost)

        # dp[i][j]: minimum cost to choose j windows from nums[:i].
        inf = float("inf")
        dp = [[inf] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x],
                    )

        return dp[n][k]
        