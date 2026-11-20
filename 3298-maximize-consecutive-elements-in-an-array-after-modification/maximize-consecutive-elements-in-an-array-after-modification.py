class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        best = {}
        answer = 0

        for x in nums:
            previous = best.get(x, 0)

            # Use x unchanged to extend a sequence ending at x - 1.
            best[x] = max(best.get(x, 0), best.get(x - 1, 0) + 1)

            # Use x + 1 to extend a sequence ending at x.
            best[x + 1] = max(best.get(x + 1, 0), previous + 1)

            answer = max(answer, best[x], best[x + 1])

        return answer