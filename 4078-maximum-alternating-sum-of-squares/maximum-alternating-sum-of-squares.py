class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted((x * x for x in nums), reverse=True)
        positive_count = (len(nums) + 1) // 2
        return sum(squares[:positive_count]) - sum(squares[positive_count:])