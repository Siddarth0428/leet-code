class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        total = 0

        for start in range(len(nums)):
            distinct = set()
            for end in range(start, len(nums)):
                distinct.add(nums[end])
                total += len(distinct) ** 2

        return total