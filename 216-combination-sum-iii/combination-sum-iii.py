class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return

            needed = k - len(path)

            # Stop when too few numbers remain or even the smallest
            # available numbers would exceed the remaining sum.
            if 10 - start < needed:
                return
            if sum(range(start, start + needed)) > remaining:
                return

            for num in range(start, 10):
                if num > remaining:
                    break
                path.append(num)
                backtrack(num + 1, remaining - num)
                path.pop()

        backtrack(1, n)
        return result