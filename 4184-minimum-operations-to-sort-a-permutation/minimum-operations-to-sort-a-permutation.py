class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0
        if n == 2:
            return 1  # The only other permutation sorts with one reverse.

        def rotation_shift(target):
            k = target.index(nums[0])
            if all(nums[i] == target[(i + k) % n] for i in range(n)):
                return k
            return None

        k = rotation_shift(list(range(n)))
        if k is not None:
            return min(n - k, k + 2)

        k = rotation_shift(list(range(n - 1, -1, -1)))
        if k is not None:
            return 1 + min(k, n - k)

        return -1