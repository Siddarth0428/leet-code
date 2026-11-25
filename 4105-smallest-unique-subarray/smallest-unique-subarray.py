from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sa = list(range(n))
        rank = nums[:]
        next_rank = [0] * n
        width = 1

        # Build the suffix array by doubling.
        while width < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + width] if i + width < n else -1
            ))

            next_rank[sa[0]] = 0
            for k in range(1, n):
                prev, curr = sa[k - 1], sa[k]
                prev_key = (
                    rank[prev],
                    rank[prev + width] if prev + width < n else -1
                )
                curr_key = (
                    rank[curr],
                    rank[curr + width] if curr + width < n else -1
                )
                next_rank[curr] = next_rank[prev] + (prev_key != curr_key)

            rank, next_rank = next_rank, rank
            if rank[sa[-1]] == n - 1:
                break
            width *= 2

        # LCP of adjacent suffixes in suffix-array order.
        position = [0] * n
        for i, start in enumerate(sa):
            position[start] = i

        lcp = [0] * n
        common = 0
        for start in range(n):
            p = position[start]
            if p == n - 1:
                common = 0
                continue

            other = sa[p + 1]
            while (start + common < n and other + common < n
                   and nums[start + common] == nums[other + common]):
                common += 1

            lcp[p] = common
            if common:
                common -= 1

        answer = n
        for p, start in enumerate(sa):
            longest_shared = 0
            if p > 0:
                longest_shared = max(longest_shared, lcp[p - 1])
            if p + 1 < n:
                longest_shared = max(longest_shared, lcp[p])

            candidate = longest_shared + 1
            if candidate <= n - start:
                answer = min(answer, candidate)

        return answer