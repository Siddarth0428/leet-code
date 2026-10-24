# The guess API is provided by LeetCode.
# It returns -1 if num is too high, 1 if too low, and 0 if correct.

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:  # result == 1
                low = mid + 1