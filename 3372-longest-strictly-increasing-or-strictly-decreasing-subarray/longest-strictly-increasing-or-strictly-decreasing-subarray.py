class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = decreasing = longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = decreasing = 1

            longest = max(longest, increasing, decreasing)

        return longest
        