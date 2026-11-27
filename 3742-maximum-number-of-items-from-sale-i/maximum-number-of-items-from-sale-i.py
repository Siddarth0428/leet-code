from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        rewards = []
        for i, (factor, _) in enumerate(items):
            free_copies = sum(
                1
                for j, (other_factor, _) in enumerate(items)
                if j != i and other_factor % factor == 0
            )
            rewards.append(free_copies)

        # dp[c] = best total from activating item types for exactly c cost
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i, (_, price) in enumerate(items):
            value = 1 + rewards[i]  # first purchased copy plus its free copies
            for cost in range(budget, price - 1, -1):
                if dp[cost - price] != -1:
                    dp[cost] = max(dp[cost], dp[cost - price] + value)

        answer = 0
        for cost, value in enumerate(dp):
            if value != -1:
                extra_copies = (budget - cost) // min_price
                answer = max(answer, value + extra_copies)

        return answer