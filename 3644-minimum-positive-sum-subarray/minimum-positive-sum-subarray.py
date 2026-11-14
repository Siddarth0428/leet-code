from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")

        for start in range(len(nums)):
            total = 0
            for end in range(start, min(start + r, len(nums))):
                total += nums[end]
                length = end - start + 1

                if length >= l and total > 0:
                    answer = min(answer, total)

        return -1 if answer == float("inf") else answer