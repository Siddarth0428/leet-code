class Solution:
    def maxLength(self, nums: list[int]) -> int:
        primes = (2, 3, 5, 7)

        def exponents(x: int) -> list[int]:
            result = []
            for p in primes:
                count = 0
                while x % p == 0:
                    count += 1
                    x //= p
                result.append(count)
            return result

        factors = [exponents(x) for x in nums]
        answer = 1

        for left in range(len(nums)):
            total = [0] * 4
            low = [float("inf")] * 4
            high = [0] * 4

            for right in range(left, len(nums)):
                for j, e in enumerate(factors[right]):
                    total[j] += e
                    low[j] = min(low[j], e)
                    high[j] = max(high[j], e)

                if all(total[j] == low[j] + high[j] for j in range(4)):
                    answer = max(answer, right - left + 1)

        return answer