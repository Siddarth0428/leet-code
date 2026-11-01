class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        two_steps_back = 0
        one_step_back = 0

        for step_cost in cost:
            current = step_cost + min(one_step_back, two_steps_back)
            two_steps_back, one_step_back = one_step_back, current

        return min(one_step_back, two_steps_back)