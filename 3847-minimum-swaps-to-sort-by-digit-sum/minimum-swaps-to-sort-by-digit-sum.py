class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        ordered = sorted(nums, key=lambda n: (digit_sum(n), n))
        target_index = {value: i for i, value in enumerate(ordered)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i]:
                continue

            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                cycle_length += 1
                j = target_index[nums[j]]

            swaps += cycle_length - 1

        return swaps