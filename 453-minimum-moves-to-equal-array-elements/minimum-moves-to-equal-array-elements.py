class Solution:
    def minMoves(self, nums: list[int]) -> int:
        smallest = min(nums)
        return sum(value - smallest for value in nums)