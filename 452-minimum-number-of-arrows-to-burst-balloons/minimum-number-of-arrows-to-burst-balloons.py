from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])

        arrows = 0
        last_arrow = None

        for start, end in points:
            if last_arrow is None or start > last_arrow:
                arrows += 1
                last_arrow = end

        return arrows