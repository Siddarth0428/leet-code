class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            speed = (left + right) // 2
            hours = sum((pile + speed - 1) // speed for pile in piles)

            if hours <= h:
                right = speed
            else:
                left = speed + 1

        return left