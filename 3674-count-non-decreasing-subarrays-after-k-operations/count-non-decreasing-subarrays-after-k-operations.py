from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        q = deque()
        cost = 0
        right = len(nums) - 1
        answer = 0

        for left in range(len(nums) - 1, -1, -1):
            while q and nums[q[-1]] <= nums[left]:
                index = q.pop()
                end = q[-1] if q else right + 1
                cost += (end - index) * (nums[left] - nums[index])

            q.append(left)

            while cost > k:
                cost -= nums[q[0]] - nums[right]
                if q[0] == right:
                    q.popleft()
                right -= 1

            answer += right - left + 1

        return answer