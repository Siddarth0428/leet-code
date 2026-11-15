from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # Indices of days whose warmer day is not known yet

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous_day = stack.pop()
                answer[previous_day] = i - previous_day

            stack.append(i)

        return answer
        