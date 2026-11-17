class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_before = 1
        two_steps_before = 1

        for _ in range(2, n + 1):
            one_step_before, two_steps_before = (
                one_step_before + two_steps_before,
                one_step_before,
            )

        return one_step_before