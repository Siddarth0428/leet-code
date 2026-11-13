from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        removals = 0
        last_end = float("-inf")

        for start, end in intervals:
            if start < last_end:
                removals += 1
            else:
                last_end = end

        return removals